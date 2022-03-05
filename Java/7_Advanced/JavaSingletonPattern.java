
class JavaSingletonPattern{
    private JavaSingletonPattern() {}
    public String str;
    private static JavaSingletonPattern singleton;
    static JavaSingletonPattern getSingleInstance() {
        if (singleton == null)
            singleton = new JavaSingletonPattern();
        
        return singleton;
    }
}