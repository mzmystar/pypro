package person;

public class EnglishTeacher extends Teacher implements SpeakEnglish{
    public void speakEnglish(){
        System.out.println("英文老师说英语");
    }
    public void major(){
        System.out.println("英文专业");
    }
}
