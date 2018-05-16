import pandas
from bokeh.plotting import figure, output_file, show


#Contiguous U.S., Precipitation, April
#Units: Inches
#Base Period: 1901-2000
#Missing: -99
#Date,Value,Anomaly 
# from: https://www.ncdc.noaa.gov/cag/national/time-series
df=pandas.read_csv("rainDataSet.csv")

p=figure(plot_width=500,plot_height=400,x_axis_type='datetime',tools='pan',logo=None)
 
p.title.text="Rain"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Time"
p.yaxis.axis_label="Rain(inches)"    
 
p.line(x, df['Value'], line_width=2)

p.vbar(x=df['Date'], width=0.5, bottom=df[Value].max()*-1,top=df['Anomaly'], color="firebrick")

output_file("AprilShowersUSA.html")
show(p)