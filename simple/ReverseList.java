class ReverseList{
    public static class Node{
        int val;
        Node next;
        public Node(int v){
           val=v;
           next=null;
        }
    }
    
    public ReverseList(){}



    public Node reverse(Node head){
  
        if (head==null){
            return head;
        }
        if (head.next==null){
            return head;
        }
        
        Node next = head.next;
        head.next = null;
        while(next!=null){
            Node second = next.next;
            next.next = head;
            head = next;
            next = second;


        }
        return head;
    }

    public void print(Node head){
        String s = "";
        while(head!=null){
            s += head.val + " - ";
            head = head.next;
        }
        System.out.println(s);
    }


    public static void main(String args[]){

        ReverseList r = new ReverseList();
        Node head = new Node(1);
        Node n2 = new Node(2);
        Node n3 = new Node(3);
        Node n4 = new Node(4);
        head.next = n2;
        n2.next = n3;
        n3.next = n4;

        r.print(head);
        Node newhead = r.reverse(head);
        r.print(newhead);


    }


}
