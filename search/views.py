from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from search.forms import MovieModel, MovieReview
from search.models import Movie, Review
from search.sevice.Movie import SearchMovieApi
from django.utils import timezone

@login_required
def review_delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.movie_info.delete()
    review.delete()
    return redirect('review_list')

@login_required
def review_edit_page(request, pk):
    cur = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = MovieReview(request.POST)
        if form.is_valid():
            cur.review=form.cleaned_data['review']
            cur.save()
            return redirect('review_list')
    else:
        form = MovieReview()
    return render(request, 'search/review_edit_page.html', {'form': form, 'data': cur.movie_info})

@login_required
def review_list(request):
    reviews = Review.objects.filter(author=request.user)
    reviews_list=[]
    for cur in reviews.iterator():
        reviews_list.append(cur)
    return render(request, 'search/review_list_page.html', {'reviews': reviews_list, 'user':request.user})

@login_required
def review_detail(request, title, number):
    search_list = SearchMovieApi.Search_Movie_title(title)
    curN = number - 1
    cur = search_list[curN]
    cur['title'] = cur['title'].replace('<b>', '')
    cur['title'] = cur['title'].replace('</b>', '')
    if request.method == 'POST':
        form = MovieReview(request.POST)
        if form.is_valid():
            clean_data_dict = form.cleaned_data
            movie = Movie.objects.create(
                author=request.user,
                number=curN,
                title=cur['title'],
                subtitle=cur['subtitle'],
                link=cur['link'],
                image=cur['image'],
                director=cur['director'],
                actor=cur['actor'],
                userRating=cur['userRating']
            )
            review = Review.objects.create(
                movie_info=movie,
                author=request.user,
                review=clean_data_dict.get('review')
            )
            return redirect('review_list')
    else:
        form = MovieReview()
    return render(request, 'search/review_page.html', {'form': form, 'data': cur})


def search_main(request):
    if (request.method == 'POST'):
        movie = MovieModel()
        # print(type(request.POST),request.POST)
        title = request.POST.get('title')
        return redirect('movie_list_page', title)
    else:
        movie = MovieModel()
    return render(request, 'search/main_page.html', {"obj": movie})

def movie_list(request, title):
    search_list = SearchMovieApi.Search_Movie_title(title)
    ret_dict_list = []
    for idx, cur in enumerate(search_list, 1):
        cur_model = Movie()
        cur_model.pk = cur.get('pk')
        #
        cur_model.number = idx

        # 제목 작업..
        temp_title = cur.get('title')
        temp_title = temp_title.replace('<b>', '')
        temp_title = temp_title.replace('</b>', '')
        cur_model.title = temp_title

        #
        cur_model.author = cur.get('author')

        #
        cur_model.subtitle = cur.get('subtitle')

        #
        cur_model.link = cur.get('link')

        #
        cur_model.image = cur.get('image')

        #
        cur_model.pubDate = cur.get('pubDate')

        #
        temp_director = cur.get('director')
        temp_director = temp_director.replace('|', ',')
        cur_model.director = temp_director

        #
        temp_actor = cur.get('actor')
        temp_actor = temp_actor.replace('|', ',')
        cur_model.actor = temp_actor

        #
        temp_userRating = cur.get('userRating')
        temp_userRating = temp_userRating
        if temp_userRating == 0:
            continue
        cur_model.userRating = cur.get('userRating')
        #
        ret_dict_list.append(cur_model)
    return render(request, 'search/movie_list_page.html', {"lists": ret_dict_list, "maintitle": title})
