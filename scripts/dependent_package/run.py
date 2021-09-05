import graphviz
import os
import json

buildrequire_filepath = os.path.join(os.getcwd(), 'buildrequiresfile.json')
inputfilepath = os.path.join(os.getcwd(), 'inputfile.json')

def get_graphdata(datafile, inputfile):
    with open(datafile, 'r') as f:
        packgedata = json.load(f)

    with open(inputfile, 'r') as f:
        inputdata = json.load(f)
    
    graphdata = []
    for pkg in inputdata['packages']:
        requiredlist = []
        requireslist = []
        print ('inputdata', inputdata)
        for data in packgedata:
            if pkg == data['packagename']:
               requireslist = data['buildrequires']
            if pkg in data['buildrequires']:
               requiredlist.append(data['packagename'])
        data_dict = dict(package=pkg, requires=requireslist, required=requiredlist)
        graphdata.append(data_dict)
    print('graphdata', graphdata)
    return graphdata

def create_graph(data):
    dot = graphviz.Digraph(comment='packges dependency table')
    packagelist = []
    for item in data:
        packagelist.append(item['package'])
        packagelist = packagelist + item['requires'] + item['required']
    packagelist = list(set(packagelist))
    print ('packagelist', packagelist)
    for pkg in packagelist:
        dot.node(pkg)
    for item in data:
        if len(item['requires']) > 0:
            for m in item['requires']:
                dot.edge(m, item['package'])
        if len(item['required']) > 0:
            for n in item['required']:
                dot.edge(item['package'], n)

    print (dot.source)
    dot.render('graph-output/packges-dependency-table.gv', view=True)

                
if __name__=="__main__":
    graphdata = get_graphdata(buildrequire_filepath, inputfilepath)
    create_graph(graphdata)


    
