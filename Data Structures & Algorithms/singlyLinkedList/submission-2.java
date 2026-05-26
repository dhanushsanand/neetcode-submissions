class Node{
    Integer val;
    Node next;

    public Node(){
        this.val = -1;
        this.next = null;
    }
    public Node(int val){
        this.val = val;
        this.next = null;
    }
}
public class LinkedList {
    Node head;
    int length=0;
    public LinkedList(){
        head = new Node();
    }

    public int get(int index){
        if(index > (length-1)) return -1;
        if(index == 0) return head.next.val;
        Node temp = head.next;
        for(int i= 0;i<index;i++){
            temp = temp.next;
        }
        return temp.val;
    }

    public boolean remove(int index){
        if(index > (length-1)) return false;
        Node temp = head.next;
        if(index == 0) head.next = head.next.next;
        else{
            while((index - 1) > 0){
                temp = temp.next;
                index--;
            }
            temp.next = temp.next.next;
        }
        length-=1;
        return true;
    }

    public void insertHead(Integer val){
        Node node = new Node(val);
        Node temp = head.next;
        head.next = node;
        node.next = temp;
        length+=1;
    }

    public void insertTail(Integer val){
        Node node = new Node(val);
        Node temp = head.next;
        if(temp == null){
            head.next = node;
        }
        else {
            while(temp.next != null){
                temp = temp.next;
            }
            temp.next = node;
        }
        length+=1;
    }

    public List<Integer> getValues(){
        List<Integer> list = new ArrayList<>();
        Node temp = head.next;
        while(temp!=null){
            list.add(temp.val);
            temp = temp.next;
        }
        return list;
    }
    }