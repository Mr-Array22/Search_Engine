from Auxiliary import *
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from tkinter import scrolledtext
from tkinter import messagebox


if __name__ == '__main__':
    docslist = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt', '8.txt', '9.txt', '10.txt']
    b = Tokenization
    index_list2={}
    index_list2=b.get_p_index_with_stemming(docslist)
    print("                  Positional Index             ")
    for x, y in index_list2.items():
        print(x, "=", y)
        
    # ------------------------------------------------------------------------------------------------------------
    print("                  	Term Frequency	               ")
    tfList = get_term_freq()
    print(tfList)
    # ------------------------------------------------------------------------------------------------------------
    print("                  	Weighted Term Frequency	               ")
    wtfList = get_weighted_term_freq()
    print(wtfList)
    # ------------------------------------------------------------------------------------------------------------
    print("                  	Inverse Document Frequency	               ")
    idfList = get_inverse_document_freq()
    print(idfList)
    # ------------------------------------------------------------------------------------------------------------
    print("                  	      TF*IDF	                           ")
    tfidfList = get_tf_idf()
    print(tfidfList)
    # ------------------------------------------------------------------------------------------------------------
    print("                                 Doc Length                      ")
    dl = get_doc_length()
    print(dl)
    # ------------------------------------------------------------------------------------------------------------
    print("                                 Normalized TF*IDF                     ")
    n = get_normalized_tfidf()
    print(n)
    # ------------------------------------------------------------------------------------------------------------
    while True:
        query = input("Please Enter The Query (type 'exit' to stop): ")
        if query.lower() == 'exit':
            break

        result = b.process_query(query, index_list2)
        if len(result) > 0:
            x = 1
        else:
            x = 0
        if x == 1:
            df1 = get_result(query, result)
            print(df1[0])
            print(df1[1])
            print("Query Length = ", df1[2])
            sorted_s = sorted(df1[3], reverse=True)
            for i in range(len(df1[3])):
                print('Cosine Similarity(q,doc', df1[4][i], ') =', df1[3][i])

            print("Returned docs", sorted_s)
        else:
            print("Try Another Query")





# -----------------------------------GUI----------------------------------------------

class InformationRetrievalGUI:
    def __init__(self, master):
        self.master = master
        master.title("Information Retrieval System")

        
        master.configure(bg='#ECECEC')  

        
        self.header_label = ttk.Label(master, text="Information Retrieval System", font=('Helvetica', 16, 'bold'), background='#ECECEC')
        self.header_label.grid(row=0, column=0, columnspan=3, pady=10)

        
        self.query_label = ttk.Label(master, text="Enter Query:", font=('Helvetica', 12), background='#ECECEC')
        self.query_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

        self.query_entry = ttk.Entry(master, width=50, font=('Helvetica', 12))
        self.query_entry.grid(row=1, column=1, padx=10, pady=10)

        
        self.search_button = ttk.Button(master, text="Search", command=self.search_query, style='TButton')
        self.search_button.grid(row=1, column=2, padx=10, pady=10)

        
        self.result_text = scrolledtext.ScrolledText(master, width=80, height=20, wrap=tk.WORD, font=('Helvetica', 12))
        self.result_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def search_query(self):
        query = self.query_entry.get()
        result = self.process_query(query)
        self.display_results(result)

    def process_query(self, query):
        
        result = b.process_query(query, index_list2)
        return result

    def display_results(self, result):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Query: {self.query_entry.get()}\n\n")
        self.result_text.insert(tk.END, f"Number of documents found: {len(result)}\n\n")
        self.result_text.insert(tk.END, "Documents:\n\n")
        if len(result) > 0:
            for doc in result:
                self.result_text.insert(tk.END, f"{doc}\n")
        else:
            messagebox.showinfo("No Results", "No documents found for the given query.")



if __name__ == "__main__":
    root = tk.Tk()
    
    
    s = ttk.Style()
    s.configure('TButton', background='#4CAF50', foreground='#FFFFFF', font=('Helvetica', 12, 'bold'))

    app = InformationRetrievalGUI(root)
    root.mainloop()

























