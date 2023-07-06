import diagram3d_usecase as d3_use
import diagram3d as d3
import EventPlot as ep
import EventPlot_usecase as ep_use
import histograms_usecase as hist_use
import histograms as hist
import histograms2d_usecase as hist2_use
import histograms2d as hist2
import Step_demo_plot as sdp
import step_demo_plot_usecase as sdp_use
import Table_Demo as td
import table_demo_usecase as td_use

def process_choice(choice):
    if choice == "Event Plot diagram":
        ep.plt.show()
    elif choice == "Event Plot diagram Use Case":
        ep_use.plt.show()
    elif choice == "Step Demo Plot":
        sdp.plt.show()
    elif choice == "Step Demo Plot Use Case":
        sdp_use.plt.show()
    elif choice == "Table Demo Diagram":
        td.plt.show()
    elif choice == "Table Demo Diagram Use Case":
        td_use.plt.show()
    elif choice == "Histograms":
        hist.plt.show()
    elif choice == "Histograms Use Case":
        hist_use.plt.show()
    elif choice == "2D Histogram":
        hist2.plt.show()
    elif choice == "2D Histogram Use Case":
        hist2_use.plt.show()
    elif choice == "3D Diagram":
        d3.plt.show()
    elif choice == "3D Diagram Use Case":
        d3_use.plt.show()

a = ["Event Plot diagram",
     "Event Plot diagram Use Case",
     "Step Demo Plot",
     "Step Demo Plot Use Case",
     "Table Demo Diagram",
     "Table Demo Diagram Use Case",
     "Histograms",
     "Histograms Use Case",
     "2D Histogram",
     "2D Histogram Use Case",
     "3D Diagram",
     "3D Diagram Use Case",]


print ('\n'.join(map(str, a)))

user_choice = int(input("Choose which chart you want: "))

process_choice(user_choice)


