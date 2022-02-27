#include <iostream>
using namespace std;
class Room{
    public:
    double length;
    double breath;
    double height;
    double calculateArea(){
        return length * breath;
    }
    double calculateVolume(){
        return length * breath * height;
    }
};
int main(){
    Room room1;
    room1.length = 42.5;
    room1.breath = 30.8;
    room1.breath = 19.2;
}
cout<<"Area of Room = "<<room1.calculateArea() << endl;
cout<<"Volume of Room = "<<room1.calculateVolume() << endl;
return 0;
}