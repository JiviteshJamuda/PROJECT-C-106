import csv 
import plotly.express as px
import numpy as np

def get_data_src(data_path):
    Temperature = []
    ice_sales = []
    with open(data_path) as csv_file:
        data = csv.DictReader(csv_file)
        for row in data :
            Temperature.append(float(row["Marks In Percentage"]))
            ice_sales.append(float(row["Days Present"]))
    return{"x":Temperature, "y":ice_sales}

def find_correlation(data) :
    correlation = np.corrcoef(data["x"],data["y"])
    print(correlation)

def plot_graph(data_path):
    with open(data_path) as csv_file :
        data = csv.DictReader(csv_file)
        graph = px.scatter(data, x="Days Present", y="Marks In Percentage")
        graph.show()

def setup():
    data_path = "data3.csv"
    data = get_data_src(data_path)
    find_correlation(data)
    plot_graph(data_path)

setup()