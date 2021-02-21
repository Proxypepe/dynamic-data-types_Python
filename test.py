from Double_linked_list import Double_list

def main():

    myList = Double_list()

    myList.push_back(12)
    myList.pop_back()
    myList.push_back(13)

    myList.push_front(1)
    myList.push_front(2)
    myList.pop_front()
    myList.push_back(14)

    for i in myList:
        print(i)



if __name__ == '__main__':
    main()
