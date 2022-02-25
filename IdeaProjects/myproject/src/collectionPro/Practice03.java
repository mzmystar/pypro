package collectionPro;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class Practice03 {
    public static void main(String[] args){
        Collection<Stu> stu = new ArrayList<>();
        Stu s1 = new Stu("学生甲",20);
        Stu s2 = new Stu("学生乙",23);
        Stu s3 = new Stu("学生丙",24);
        stu.add(s1);stu.add(s2);stu.add(s3);
        Iterator<Stu> it = stu.iterator();
        while (it.hasNext()){
            Stu s = it.next();
            System.out.println(s.getName()+"    "+s.getAge());
        }
    }

}