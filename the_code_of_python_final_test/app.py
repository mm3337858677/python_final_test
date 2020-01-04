from flask import Flask, render_template, request, escape
from salary import timeline_bar, salary_map, wordcloud_diamond, overlap_line_scatter, wordcloud_diamond, bar_base_with_animation
from jinja2 import Markup
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line,Scatter, Timeline, Map,WordCloud



app = Flask(__name__)

area = ['animation','salary','diamond','scatter','wordcloud']
dc = pd.read_csv("salary_data/city_salary.csv",index_col="地区",encoding='gbk')
da = pd.read_csv("salary_data/teacher_number.csv",encoding='gbk')
db = pd.read_csv("salary_data/edu_money.csv",index_col="地区",encoding='gbk')
dd = pd.read_csv("salary_data/teacher_salary.csv",encoding='gbk')






@app.route('/',methods=['GET','POST'])
def timeline() -> 'html':
    d = timeline_bar()
    plot_all = d.render_embed()
    da_str = da.to_html()
    return render_template('index.html',
                           echart = plot_all,
                           the_select_region = area,
                           the_res=da_str,
                           the_title='你好，这里是对教师工资研究数据的分析',
                           )

@app.route('/animation',methods=['GET','POST'])
def animation():
    d = bar_base_with_animation()
    plot_all = d.render_embed()
    db_str = db.to_html()
    return render_template('index.html',
                           echart = plot_all,
                           the_select_region = area,
                           the_res = db_str,
                           the_title='你好，这里是对教师工资研究数据的分析',
                           )

@app.route('/salary',methods=['GET','POST'])
def salary():
    d = salary_map()
    plot_all = d.render_embed()
    dc_str = dc.to_html()
    return render_template('index.html',
                           echart = plot_all,
                           the_select_region = area,
                           the_res = dc_str,
                           the_title='你好，这里是对教师工资研究数据的分析',
                           )
@app.route('/diamond',methods=['GET','POST'])
def diamond():
    d = wordcloud_diamond()
    plot_all = d.render_embed()
    return render_template('index.html',
                           echart = plot_all,
                           the_select_region = area,
                           the_title='你好，这里是对教师工资研究数据的分析',
                           )

@app.route('/scatter',methods=['GET','POST'])
def scatter():
    d = overlap_line_scatter()
    plot_all = d.render_embed()
    dd_str = dd.to_html()
    return render_template('index.html',
                           echart = plot_all,
                           the_select_region = area,
                           the_res = dd_str,
                           the_title='你好，这里是对教师工资研究数据的分析',
                           )

@app.route('/wordcloud')
def wordcloud():
    d = wordcloud_diamond()
    plot_all = d.render_embed()
    return render_template('index.html',
                           echart = plot_all,
                           the_select_region = area,
                           the_title='你好，这里是对教师工资研究数据的分析',
                           )

@app.route('/user',methods=['GET','POST'])
def user():

    return render_template('base2.0.html',
                           the_title='你好，这里是对教师工资研究数据的分析',


                          )

if __name__ == '__main__':
    app.run()
