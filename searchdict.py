#import the module
import cheggDict
#ask the user for the term.
term = input("What do you want to search for? ")
#get the list of results by calling the function in cheggDict module.
papers = cheggDict.search_papers(term,cheggDict.term_index)
#get the length of the list.
length = len(papers)
#print the message.
print("There are %d papers that match your search" % length)

#if there are matching papers,print out its ID and title.
if(length != 0):
    for paperid in papers:
        print(paperid, cheggDict.paper_titles[paperid])






