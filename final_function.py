import csv, sys
from sort_filter import sort_by, filter_by, filter_by_70, filter_by_boxoffice, sort_by_runtime, sort_by_boxoffice
from compare import compare_runtime, compare_awards_num, compare_box, compare_imdb
from add_item import add_film
from high_score import high
from manipulating import complete_data

t_f=False



function = sys.argv[1]
argument=sys.argv[2]
third_parameter=''
fourth_parameter=''
fifth_parameter=''

if (len(sys.argv)>3) and sys.argv[3]=='rev': 
    t_f=True 
elif (len(sys.argv)>3) and 'Oscars' in sys.argv[3] :
    third_parameter='Won'
elif (len(sys.argv)>3):  # and sys.argv[1]=='filter':
    third_parameter=str(sys.argv[3])
if (len(sys.argv)>4): 
    fourth_parameter=sys.argv[4]
if (len(sys.argv)>5): 
    fifth_parameter=sys.argv[5]
    
if __name__ == "__main__":
    if function =='complete' and argument=='data':
        complete_data()
    elif function=='sort' and argument== 'runtime':
        sort_by_runtime(t_f)
    elif function=='sort' and argument=='box_office':
        sort_by_boxoffice(t_f)
    elif function== 'sort':
        sort_by(argument,t_f)
    elif function== 'filter' and argument=='nominations':    
        filter_by_70()
    elif function== 'filter' and argument=='hundred_milion':    
        filter_by_boxoffice()
    elif function== 'filter':
        filter_by(argument,third_parameter)
    elif function == 'compare_runtime':
        compare_runtime( argument, third_parameter,fourth_parameter)
    elif function == 'compare_awards':
        compare_awards_num(argument, third_parameter)
    elif function == 'compare_boxoffice':
        compare_box(argument, third_parameter)
    elif function == 'compare_imdb':
        compare_imdb(argument, third_parameter)
    elif function == 'add_film':
        add_film(argument, third_parameter)
    elif function == 'high':
        high()
    else:
        print("Sorry unknow command")