from unittest import result
import plotly.figure_factory as ff
import random
count=[]
dice_result = []
for i in range(0, 100):
    studentperform = random.randint(1, 6)
    studentperform = random.randint(1, 6)
    studentperform_result.append(studentperform + studentperform)
    count.append(i)




import statistics as st
mean=st.mean( studentperform_result)
mode=st.mode( studentperform_result)
median=st.median( studentperform_result) 
sd=st.stdev(studentperform_result)
print(mean,median,mode)
sd1start,sd1end=mean-sd,mean+sd
sd2start,sd2end=mean-(2*sd),mean+(2*sd)
sd3start,sd3end=mean-(3*sd),mean+(3*sd)
import plotly.graph_objects as go
fig = ff.create_distplot([studentperform_result], ["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="sd2"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="sd2"))

fig.show()
sd1list=[result for result in studentperform_result if result>sd1start  and result<sd1end]
sd2list=[result for result in studentperform_result if result>sd2start  and result<sd2end]
sd3list=[result for result in studentperform_result if result>sd3start  and result<sd3end]
print("{}% of data lies within sd1 ".format(len(sd1list)*100.0/len(studentperform_result)))
print("{}% of data lies within sd2 ".format(len(sd2list)*100.0/len(studentperform_result)))
print("{}% of data lies within sd3 ".format(len(sd3list)*100.0/len(studentperform_result)))