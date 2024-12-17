from flask import Flask as fl, render_template
from time import time
import numpy as np  # Import moved to the top
import datetime as d
import math
import Algoritma
import Algoritma2

app = fl(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dynamic/')
@app.route('/dynamic/<str_A>/<str_B>')
def dynamic(str_A=None, str_B=None):
    if str_A:
        # Convert strings to numpy arrays
        A = np.fromstring(str_A, dtype='|S1')
        B = np.fromstring(str_B, dtype='|S1')

        # Start timing
        start_time = time()

        # Run edit distance algorithm
        ED1, ptrl, edInt, newA, newB = Algoritma.edit_distance(A, B)

        # End timing
        execution_time = time() - start_time

        # Prepare results for rendering
        ED1 = ED1.tolist()
        ptrl = ptrl.tolist()
        arr_A = list(str_A)
        arr_B = list(str_B)

        for idx, zz in enumerate(newA):
            if newA[idx] == '-':
                newA[idx] = newA[idx]
            else:
                newA[idx] = newA[idx].decode('utf-8')

        for idx, zz in enumerate(newB):
            if newB[idx] == '-':
                newB[idx] = newB[idx]
            else:
                newB[idx] = newB[idx].decode('utf-8')

        return render_template("dynamic-traceback.html",
                               EDI=ED1, PTR=ptrl, str_A=str_A, str_B=str_B,
                               arr_A=arr_A, arr_B=arr_B, edInt=edInt,
                               newA=newA, newB=newB, execution_time=f"{execution_time:.6f}s")
    else:
        A = np.fromstring("", dtype='|S1')
        B = np.fromstring("", dtype='|S1')
        ED1, ptrl, edInt, newA, newB = Algoritma.edit_distance(A, B)
        ED1 = ED1.tolist()
        ptrl = ptrl.tolist()
        return render_template("dynamic-traceback.html", EDI=ED1, PTR=ptrl, str_A=str_A, str_B=str_B)

@app.route('/dynamicwithouttraceback/')
@app.route('/dynamicwithouttraceback/<str_A>/<str_B>')
def dynamic_wotr(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        ED2, ed2, tr2, newA, newB = Algoritma.edit_distance_wotr(str_A, str_B)
        ED2 = ED2.tolist()
        arr_A = list(str_A)
        arr_B = list(str_B)

        for idx, zz in enumerate(newA):
            if newA[idx] == '-':
                newA[idx] = newA[idx]
            else:
                newA[idx] = newA[idx].decode('utf-8')

        for idx, zz in enumerate(newB):
            if newB[idx] == '-':
                newB[idx] = newB[idx]
            else:
                newB[idx] = newB[idx].decode('utf-8')

        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "dynamic-without-traceback.html",
            EDI=ED2, tr2=tr2, str_A=str_A, str_B=str_B, arr_A=arr_A, arr_B=arr_B,
            edInt=ed2, newA=newA, newB=newB, execution_time=f"{execution_time:.6f}s"
        )
    else:
        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "dynamic-without-traceback.html",
            str_A=str_A, str_B=str_B, execution_time=f"{execution_time:.6f}s"
        )

@app.route('/dynamicalternative/')
@app.route('/dynamicalternative/<str_A>/<str_B>')
def dynamic_alt(str_A=None, str_B=None):
    if str_A:
        ed2, ED2, n1, n2 = Algoritma.LevenshteinDistance(str_A, str_B)
        arr_A = list(str_A)
        arr_B = list(str_B)
        return render_template("dynamicalternative.html", EDI=ED2, str_A=str_A, str_B=str_B, edInt=ed2, arr_A=arr_A, arr_B=arr_B)
    else:
        return render_template("dynamicalternative.html", str_A=str_A, str_B=str_B)
    
# Greedy - Fast Approach
@app.route('/greedy/')
@app.route('/greedy/<str_A>/<str_B>')
def greedy(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        # Execute the Greedy Algorithm
        ed2 = Algoritma.ed_greedy(str_A, str_B)

        # Prepare data for rendering
        arr_A = list(str_A)
        arr_B = list(str_B)

        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "greedy-fast.html",
            str_A=str_A, str_B=str_B, edInt=ed2,
            arr_A=arr_A, arr_B=arr_B, execution_time=f"{execution_time:.6f}s"
        )
    else:
        execution_time = time() - start_time  # Calculate execution time for default case
        return render_template(
            "greedy-fast.html",
            str_A=str_A, str_B=str_B, execution_time=f"{execution_time:.6f}s"
        )
        
@app.route('/greedyalternative/')
@app.route('/greedyalternative/<str_A>/<str_B>')
def greedyalt(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        # Execute the Greedy LCS Algorithm
        ed2 = Algoritma.editDistanceGreedy(str_A, str_B)

        # Prepare data for rendering
        arr_A = list(str_A)
        arr_B = list(str_B)

        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "greedyalt.html",
            str_A=str_A, str_B=str_B, edInt=ed2,
            arr_A=arr_A, arr_B=arr_B, execution_time=f"{execution_time:.6f}s"
        )
    else:
        execution_time = time() - start_time  # Calculate execution time for default case
        return render_template(
            "greedyalt.html",
            str_A=str_A, str_B=str_B, execution_time=f"{execution_time:.6f}s"
        )



@app.route('/divideandconquer/')
@app.route('/divideandconquer/<str_A>/<str_B>')
def dividenc(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        # Execute the Divide and Conquer Edit Distance algorithm
        ed2, newA, newB, s1 = Algoritma.Divide_and_Conquer_ED(str_A, str_B)
        
        # Prepare data for rendering
        arr_A = list(str_A)
        arr_B = list(str_B)
        
        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "divideandconquer.html",
            str_A=str_A, str_B=str_B, edInt=ed2,
            arr_A=arr_A, arr_B=arr_B, newA=newA,
            newB=newB, s1=s1, execution_time=f"{execution_time:.6f}s"
        )
    else:
        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "divideandconquer.html",
            str_A=str_A, str_B=str_B, execution_time=f"{execution_time:.6f}s"
        )

@app.route('/divideandconquer2/')
@app.route('/divideandconquer2/<str_A>/<str_B>')
def dividencrv2(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        # Execute Divide and Conquer Version 2
        ed2, newA, newB, s1 = Algoritma.divide_conquer_version2(str_A, str_B)

        # Prepare data for rendering
        arr_A = list(str_A)
        arr_B = list(str_B)

        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "divideandconquer2.html",
            str_A=str_A, str_B=str_B, edInt=ed2,
            arr_A=arr_A, arr_B=arr_B, newA=newA,
            newB=newB, s1=s1, execution_time=f"{execution_time:.6f}s"
        )
    else:
        execution_time = time() - start_time  # Calculate execution time for default case
        return render_template(
            "divideandconquer2.html",
            str_A=str_A, str_B=str_B, execution_time=f"{execution_time:.6f}s"
        )
        
@app.route('/stripek/')
@app.route('/stripek/<str_A>/<str_B>')
def stripe(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        # Execute the Stripe-K Edit Distance Algorithm
        ed2, newA, newB, ED1, ptrl, k = Algoritma.stripe_edit_distance(str_A, str_B)

        # Prepare data for rendering
        arr_A = list(str_A)
        arr_B = list(str_B)

        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "stripek.html",
            str_A=str_A,
            str_B=str_B,
            edInt=ed2,
            arr_A=arr_A,
            arr_B=arr_B,
            newA="".join(newA),  # Convert aligned strings back to a single string
            newB="".join(newB),
            EDI=ED1.tolist(),  # Convert numpy array to list for rendering
            PTR=ptrl.tolist(),  # Convert traceback array to list
            k=k,
            execution_time=f"{execution_time:.6f}s"  # Display execution time
        )
    else:
        execution_time = time() - start_time  # Calculate execution time for default case
        return render_template(
            "stripek.html",
            str_A=str_A,
            str_B=str_B,
            execution_time=f"{execution_time:.6f}s"
        )

@app.route('/recursive/')
@app.route('/recursive/<str_A>/<str_B>')
def recursive(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        # Compute edit distance and alignment
        (ed2_value, path), (newA, newB) = Algoritma.rec_ed_with_path_and_alignment(str_A, str_B)

        # Prepare list representations of the strings
        arr_A = list(str_A)
        arr_B = list(str_B)

        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "recursive.html",
            str_A=str_A,
            str_B=str_B,
            edInt=ed2_value,  # Edit Distance Value
            arr_A=arr_A,
            arr_B=arr_B,
            newA="".join(newA),  # Convert aligned A to string
            newB="".join(newB),  # Convert aligned B to string
            path=" -> ".join(path),  # Display the path steps
            execution_time=f"{execution_time:.6f}s"  # Execution time
        )
    else:
        execution_time = time() - start_time  # Calculate execution time for default case
        return render_template(
            "recursive.html",
            str_A=str_A,
            str_B=str_B,
            execution_time=f"{execution_time:.6f}s"
        )

@app.route('/branchandboundwithpath/')
@app.route('/branchandboundwithpath/<str_A>/<str_B>')
def branchandboundwithpath(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        ed2, (newA, newB) = Algoritma.ed_bb_with_path_and_alignment(str_A, str_B)
        
        # Calculate execution time
        execution_time = time() - start_time
        
        arr_A = list(str_A)
        arr_B = list(str_B)
        return render_template(
            "branchandboundwithpath.html", 
            str_A=str_A, 
            str_B=str_B, 
            edInt=ed2, 
            arr_A=arr_A, 
            arr_B=arr_B, 
            newA=newA, 
            newB=newB,
            execution_time=f"{execution_time:.6f}s"  # Format execution time to 6 decimal places
        )
    else:
        # Calculate execution time for default case
        execution_time = time() - start_time
        return render_template(
            "branchandboundwithpath.html", 
            str_A=str_A, 
            str_B=str_B,
            execution_time=f"{execution_time:.6f}s"
        )
        
@app.route('/branchandboundwithqueue/')
@app.route('/branchandboundwithqueue/<str_A>/<str_B>')
def branchandboundwithqueue(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        # Call the Branch_and_Bound function and get results
        ed2, newA, newB = Algoritma2.Branch_and_Bound(str_A, str_B)

        # Prepare list representations of the strings
        arr_A = list(str_A)
        arr_B = list(str_B)

        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "branchandboundwithqueue.html",
            str_A=str_A,
            str_B=str_B,
            edInt=ed2,  # Edit Distance Value
            arr_A=arr_A,
            arr_B=arr_B,
            newA="".join(newA),  # Convert aligned A to string
            newB="".join(newB),  # Convert aligned B to string
            execution_time=f"{execution_time:.6f}s"  # Execution time
        )
    else:
        execution_time = time() - start_time  # Calculate execution time for default case
        return render_template(
            "branchandboundwithqueue.html",
            str_A=str_A,
            str_B=str_B,
            execution_time=f"{execution_time:.6f}s"
        )


@app.route('/backtracking/')
@app.route('/backtracking/<str_A>/<str_B>')
def backtracking_edit_distance(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        # Execute Backtracking Edit Distance Algorithm
        ed_result, (newA, newB) = Algoritma.ed_backtracking_wrapper(str_A, str_B)

        # Prepare data for rendering
        arr_A = list(str_A)
        arr_B = list(str_B)

        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "backtracking.html",
            str_A=str_A, 
            str_B=str_B, 
            edInt=ed_result,  # Edit distance
            arr_A=arr_A, 
            arr_B=arr_B, 
            newA=newA,  # Aligned string A
            newB=newB,  # Aligned string B
            execution_time=f"{execution_time:.6f}s"
        )
    else:
        execution_time = time() - start_time  # Calculate execution time for default case
        return render_template(
            "backtracking.html",
            str_A=str_A, 
            str_B=str_B, 
            execution_time=f"{execution_time:.6f}s"
        )


@app.route('/bfs/')
@app.route('/bfs/<str_A>/<str_B>')
def bfs_edit_distance(str_A=None, str_B=None):
    start_time = time()  # Start timing

    if str_A:
        # Execute BFS Edit Distance Algorithm
        ed_result, (newA, newB) = Algoritma.ed_bfs_wrapper(str_A, str_B)

        # Prepare data for rendering
        arr_A = list(str_A)
        arr_B = list(str_B)

        execution_time = time() - start_time  # Calculate execution time
        return render_template(
            "bfs.html",
            str_A=str_A, 
            str_B=str_B, 
            edInt=ed_result,  # Edit distance
            arr_A=arr_A, 
            arr_B=arr_B, 
            newA=newA,  # Aligned string A
            newB=newB,  # Aligned string B
            execution_time=f"{execution_time:.6f}s"
        )
    else:
        execution_time = time() - start_time  # Calculate execution time for default case
        return render_template(
            "bfs.html",
            str_A=str_A, 
            str_B=str_B, 
            execution_time=f"{execution_time:.6f}s"
        )


if __name__ == "__main__":
    app.run()

