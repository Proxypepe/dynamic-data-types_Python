from Double_linked_list import DoubleList
from Forward_list import ForwardList

def main():

    # myList = DoubleList()
    #
    # myList.push_back(12)
    #
    # myList.insert_before(1, 100)
    # print(f"len: {len(myList)}")
    # # myList.insert_after(len(myList), 101)
    # # myList.emplace_back(1, 2, 3)
    #
    # print(f"len: {len(myList)}")

    # myList = ForwardList()
    myList = ForwardList()
    
    myList.push_back(10)
    myList.push_back(12)
    myList.push_back(13)
    myList.push_back(14)
    myList.push_back(15)
    myList.erase(4)
    myList.push_back()

    for i in myList:
        print(i)


if __name__ == '__main__':
    main()
