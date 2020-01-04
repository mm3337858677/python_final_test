import pandas as pd
#from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line,Scatter, Timeline, Map,WordCloud

da = pd.read_csv("salary_data/teacher_number.csv",encoding='gbk')



province_a = list(da['地区'])
# province_a
number_2018 = list(da['2018年'])
# number_2018
number_2017 = list(da['2017年'])
# number_2017
number_2016 = list(da['2016年'])
# number_2016
number_2015 = list(da['2015年'])
# number_2015
number_2014 = list(da['2014年'])
# number_2014

def timeline_bar(province=None) -> Timeline:
    x = province
    tl = Timeline()
    bar = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("年份", number_2014)
            .set_global_opts(title_opts=opts.TitleOpts("{}年全国各省高校教职工人数(万人)".format('2014')))
    )
    tl.add(bar, "{}年".format('2014'))

    bar1 = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("年份", number_2015)

            .set_global_opts(title_opts=opts.TitleOpts("{}年全国各省高校教职工人数(万人)".format('2015')))
    )
    tl.add(bar1, "{}年".format('2015'))

    bar2 = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("年份", number_2016)

            .set_global_opts(title_opts=opts.TitleOpts("{}年全国各省高校教职工人数(万人)".format('2016')))
    )
    tl.add(bar2, "{}年".format('2016'))

    bar3 = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("年份", number_2017)

            .set_global_opts(title_opts=opts.TitleOpts("{}年全国各省高校教职工人数(万人)".format('2017')))
    )
    tl.add(bar3, "{}年".format('2017'))

    bar4 = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("年份", number_2018)

            .set_global_opts(title_opts=opts.TitleOpts("{}年全国各省高校教职工人数(万人)".format('2018')))
    )
    tl.add(bar4, "{}年".format('2018'))
    return tl


# a = timeline_bar()
# a.render_notebook()

# 教育经费

db = pd.read_csv("salary_data/edu_money.csv",index_col="地区",encoding='gbk')
# db
# x轴 = df.columns.values
#x轴 = df.columns.values
x = [int(x)for x in db.columns.values] #列表推导
# x轴
beijing =list(db.loc["北京"].values)
# 北京
xingjiang =list(db.loc["新疆"].values)
# 新疆
def bar_base_with_animation() -> Bar:
    c = (
        Bar(
            init_opts=opts.InitOpts(
                animation_opts=opts.AnimationOpts(
                    animation_delay=1000, animation_easing="elasticOut"
                )
            )
        )
        .add_xaxis(x)
        .add_yaxis("北京", beijing)
        .add_yaxis("新疆", xingjiang)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="北京与新疆教育经费支出对比", subtitle="缺2012年及2018年")
        )
    )
    return c
# a=bar_base_with_animation() 检验数据可视化的代码
# a.render_notebook()

# 城镇平均工资
dc = pd.read_csv("salary_data/city_salary.csv",index_col="地区",encoding='gbk')
# dc
province_c = list(da['地区'])
# province_c
salary_2018 = list(dc['2018年'])
# salary_2018
salary_2017 = list(dc['2017年'])
# salary_2017
salary_2016 = list(dc['2016年'])
# salary_2016
salary_2015 = list(dc['2015年'])
# salary_2015
salary_2014 = list(dc['2014年'])
# salary_2014
分省工资_2014=[list(z) for z in zip(province_c, salary_2014)]
# 分省工资_2014
分省工资_2015=[list(z) for z in zip(province_c, salary_2015)]
# 分省工资_2015
分省工资_2015 = list(zip(list(province_c),list(salary_2015)))
# print(分省工资_2015)
分省工资_2016 = list(zip(list(province_c),list(salary_2016)))
# print(分省工资_2016)
def salary_map() -> Timeline:
    # x = regions
    tl = Timeline()

    map0 = (
        Map()
            .add("城镇平均工资水平", [list(z) for z in zip(province_c, salary_2014)], "china")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="城镇平均工资水平"),
            visualmap_opts=opts.VisualMapOpts(min_=50000, max_=120000, is_piecewise=True), ))
    tl.add(map0, "{}年".format('2014'))

    map1 = (
        Map()
            .add("城镇平均工资水平", [list(z) for z in zip(province_c, salary_2015)], "china")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="城镇平均工资水平"),
            visualmap_opts=opts.VisualMapOpts(min_=50000, max_=120000, is_piecewise=True), ))

    tl.add(map1, "{}年".format('2015'))

    map2 = (
        Map()
            .add("城镇平均工资水平", [list(z) for z in zip(province_c, salary_2016)], "china")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="城镇平均工资水平"),
            visualmap_opts=opts.VisualMapOpts(min_=50000, max_=120000, is_piecewise=True), ))
    tl.add(map2, "{}年".format('2016'))

    map3 = (
        Map()
            .add("城镇平均工资水平", [list(z) for z in zip(province_c, salary_2017)], "china")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="城镇平均工资水平"),
            visualmap_opts=opts.VisualMapOpts(min_=50000, max_=120000, is_piecewise=True),
        )
    )
    tl.add(map3, "{}年".format('2017'))

    map4 = (
        Map()
            .add("城镇平均工资水平", [list(z) for z in zip(province_c, salary_2018)], "china")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="城镇平均工资水平"),
            visualmap_opts=opts.VisualMapOpts(min_=50000, max_=120000, is_piecewise=True),
        )
    )
    tl.add(map4, "{}年".format('2018'))

    return tl

# 城镇工资对比
# a = salary_map()
# a.render_notebook()
words=list(zip(list(province_c),list(salary_2018)))
# print(words)
def wordcloud_diamond() -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[10, 100])
        .set_global_opts(title_opts=opts.TitleOpts(title="2018年城镇工资水平各省对比"))
    )
    return c
# a=wordcloud_diamond()
# a.render_notebook()

dd = pd.read_csv("salary_data/teacher_salary.csv",encoding='gbk')
dd
region=list(dd['region'])
# region
teacher_sal_2018 = list(dd['2018'])
# teacher_sal_2018
teacher_sal_2017 = list(dd['2017'])
# teacher_sal_2017
teacher_sal_2016 = list(dd['2016'])
# teacher_sal_2016
teacher_sal_2015 = list(dd['2015'])
# teacher_sal_2015
teacher_sal_2014 = list(dd['2014'])
# teacher_sal_2014
def overlap_line_scatter() -> Bar:
    x = region
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("2017", teacher_sal_2017)
        .add_yaxis("2018",teacher_sal_2018)
        .set_global_opts(title_opts=opts.TitleOpts(title="2017年及2018年教师工资情况变化"))
    )
    line = (
        Line()
        .add_xaxis(x)
        .add_yaxis("2017", teacher_sal_2017)
        .add_yaxis("2018",teacher_sal_2018)
    )
    bar.overlap(line)
    return bar
# a=overlap_line_scatter()
# a.render_notebook()
# 世界工资
words=list(zip(list(region),list(teacher_sal_2018)))
# print(words)
from pyecharts.charts import WordCloud

def wordcloud_diamond() -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[10, 100])
        .set_global_opts(title_opts=opts.TitleOpts(title="2018年教师工资水平各省对比"))
    )
    return c
# a=wordcloud_diamond()
# a.render_notebook()




