from django.shortcuts import render, redirect, reverse
from . import newbit
from .models import News
from django.db.models import Count, Q


# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {'query': list(News.objects.values_list('query', flat=True).distinct())
                                                })


def dashboard(request):
    query = list(News.objects.values_list('query', flat=True).distinct())
    query1 = request.GET.get('q1')
    query2 = request.GET.get('q2')
    cat = request.GET.get('cat')
    if cat:
        pie = News.objects.values('cat_selected').annotate(total=Count('cat_selected')).filter(query=query1).filter(
            cat_selected=cat)
        horizontalBar = News.objects.values('company').annotate(total=Count('company')).order_by('-total').filter(
            query=query1).filter(cat_selected=cat)

        # 시계열 그래프
        ts = News.objects.values('date').annotate(total=Count('date')).order_by('date_tmp').filter(query=query1).filter(
            cat_selected=cat)
        ts_form1 = []
        for time in ts:
            tmp_dick1 = {}
            tmp_dick1['date'] = f'''{time['date'].year}-{time['date'].month}-{time['date'].day}'''
            tmp_dick1['total'] = time['total']
            ts_form1.append(tmp_dick1)

        # word cloud
        word_cloud = []
        tmp_wc = News.objects.values('tokenized_doc').filter(query=query1).filter(cat_selected=cat)
        for noun in tmp_wc:
            word_cloud.append(noun['tokenized_doc'])

        # topic 리스트 입니다.
        news1 = News.objects.all().filter(query=query1).filter(represent=1).filter(cat_selected=cat).order_by(
            '-date_tmp')
        numofArticle = News.objects.all().annotate(total=Count('id')).filter(query=query1).filter(
            cat_selected=cat).count
        numofTopic = News.objects.all().annotate(total=Count('id')).filter(query=query1).filter(represent=1).filter(
            cat_selected=cat).count

        # article
        context = {'query': query,
                   'query1': query1,
                   'ts': ts_form1,
                   'pie': pie,
                   'horizontalBar': horizontalBar,
                   'word_cloud': word_cloud,
                   'news1': news1,
                   'cat': cat,
                   'num1': numofArticle,
                   'num2': numofTopic,
                   }

        if query2:
            pie2 = News.objects.values('cat_selected').annotate(total=Count('cat_selected')).filter(
                query=query2).filter(cat_selected=cat)
            horizontalBar2 = News.objects.values('company').annotate(total=Count('company')).order_by('-total').filter(
                query=query2).filter(cat_selected=cat)

            # 시계열 그래프
            ts2 = News.objects.values('date').annotate(total=Count('date')).order_by('date_tmp').filter(
                query=query2).filter(cat_selected=cat)
            ts_form2 = []
            for time in ts2:
                tmp_dick2 = {}
                tmp_dick2['date'] = f'''{time['date'].year}-{time['date'].month}-{time['date'].day}'''
                tmp_dick2['total'] = time['total']
                ts_form2.append(tmp_dick2)

            # word cloud
            word_cloud2 = []
            tmp_wc = News.objects.values('tokenized_doc').filter(query=query2).filter(cat_selected=cat)
            for noun in tmp_wc:
                word_cloud2.append(noun['tokenized_doc'])
            # topic list입니다.
            print('query2파트입니다' + cat)
            news2 = News.objects.all().filter(query=query2).filter(represent=1).filter(cat_selected=cat).order_by(
                'date_tmp')
            sum1 = News.objects.all().annotate(total=Count('id')).filter(Q(query=query1) | Q(query=query2)).filter(
                cat_selected=cat).count
            sum2 = News.objects.all().annotate(total=Count('id')).filter(Q(query=query1) | Q(query=query2)).filter(
                represent=1).filter(cat_selected=cat).count

            context['query2'] = query2
            context['ts2'] = ts_form2
            context['pie2'] = pie2
            context['horizontalBar2'] = horizontalBar2
            context['word_cloud2'] = word_cloud2
            context['news2'] = news2
            context['sum1'] = sum1
            context['sum2'] = sum2
    else:
        pie = News.objects.values('cat_selected').annotate(total=Count('cat_selected')).filter(query=query1)
        horizontalBar = News.objects.values('company').annotate(total=Count('company')).order_by('-total').filter(
            query=query1)

        # 시계열 그래프
        ts = News.objects.values('date').annotate(total=Count('date')).order_by('date_tmp').filter(query=query1)
        ts_form1 = []
        for time in ts:
            tmp_dick1 = {}
            tmp_dick1['date'] = f'''{time['date'].year}-{time['date'].month}-{time['date'].day}'''
            tmp_dick1['total'] = time['total']
            ts_form1.append(tmp_dick1)

        # word cloud
        word_cloud = []
        tmp_wc = News.objects.values('tokenized_doc').filter(query=query1)
        for noun in tmp_wc:
            word_cloud.append(noun['tokenized_doc'])

        # topic 리스트 입니다.
        news1 = News.objects.all().filter(query=query1).filter(represent=1).order_by('-date')
        numofArticle = News.objects.all().annotate(total=Count('id')).filter(query=query1).count
        numofTopic = News.objects.all().annotate(total=Count('id')).filter(query=query1).filter(represent=1).count
        # article =  #TODO
        context = {'query1': query1,
                   'ts': ts_form1,
                   'pie': pie,
                   'horizontalBar': horizontalBar,
                   'word_cloud': word_cloud,
                   'news1': news1,
                   'cat': cat,
                   'num1': numofArticle,
                   'num2': numofTopic,
                   'query': query,
                  }

        if query2:
            pie2 = News.objects.values('cat_selected').annotate(total=Count('cat_selected')).filter(query=query2)
            horizontalBar2 = News.objects.values('company').annotate(total=Count('company')).order_by('-total').filter(
                query=query2)

            # 시계열 그래프
            ts2 = News.objects.values('date').annotate(total=Count('date')).order_by('date_tmp').filter(query=query2)
            ts_form2 = []
            for time in ts2:
                tmp_dick2 = {}
                tmp_dick2['date'] = f'''{time['date'].year}-{time['date'].month}-{time['date'].day}'''
                tmp_dick2['total'] = time['total']
                ts_form2.append(tmp_dick2)

            # word cloud
            word_cloud2 = []
            tmp_wc = News.objects.values('tokenized_doc').filter(query=query2)
            for noun in tmp_wc:
                word_cloud2.append(noun['tokenized_doc'])
            # topic list입니다.
            news2 = News.objects.all().filter(query=query2).filter(represent=1).order_by('-date')
            sum1 = News.objects.all().annotate(total=Count('id')).filter(Q(query=query1) | Q(query=query2)).count
            sum2 = News.objects.all().annotate(total=Count('id')).filter(Q(query=query1) | Q(query=query2)).filter(
                represent=1).count

            context['query2'] = query2
            context['ts2'] = ts_form2
            context['pie2'] = pie2
            context['horizontalBar2'] = horizontalBar2
            context['word_cloud2'] = word_cloud2
            context['news2'] = news2
            context['sum1'] = sum1
            context['sum2'] = sum2
    return render(request, 'pages/dashboard.html', context)


def about(request):
    return render(request, 'pages/about.html')


def topic(request, article_id):
    article = News.objects.get(id=article_id)
    same_topic = News.objects.filter(query=article.query).filter(cat_selected=article.cat_selected).filter(
        topic=article.topic).order_by('-date')
    wc_topic = News.objects.values('tokenized_doc').filter(query=article.query).filter(
        cat_selected=article.cat_selected).filter(topic=article.topic)
    word_cloud3 = []
    for noun in wc_topic:
        word_cloud3.append(noun['tokenized_doc'])

    context = {
        'article': article,
        'same_topic': same_topic,
        'word_cloud3': word_cloud3,
    }
    return render(request, 'pages/topic.html', context)


def article(request, article_id):
    article = News.objects.get(id=article_id)
    return render(request, 'pages/article.html', {
        'article': article,
    })
    return render(request, 'pages/topic.html', context)
