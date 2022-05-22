#include <iostream>
#include <string>

using namespace std;

class Rubik {
    public :
        // f b u d r l
        string color; 
            
        char temp;
        
        Rubik(string c) {
            color=c;
        }
    
        void F() {
            temp=color[3];
            color[3]=color[2];
            color[2]=color[1];
            color[1]=color[0];
            color[0]=temp;

            temp=color[11];
            color[11]=color[22];
            color[22]=color[13];
            color[13]=color[16];
            color[16]=temp;

            temp=color[21];
            color[21]=color[12];
            color[12]=color[19];
            color[19]=color[10];
            color[10]=temp;           
        }
        
        void R() {
            temp=color[19];
            color[19]=color[18];
            color[18]=color[17];
            color[17]=color[16];
            color[16]=temp;

            temp=color[2];
            color[2]=color[14];
            color[14]=color[4];
            color[4]=color[10];
            color[10]=temp;

            temp=color[1];
            color[1]=color[13];
            color[13]=color[7];
            color[7]=color[9];
            color[9]=temp;
        }

        void U() {
            temp=color[11];
            color[11]=color[10];
            color[10]=color[9];
            color[9]=color[8];
            color[8]=temp;

            temp=color[1];
            color[1]=color[17];
            color[17]=color[5];
            color[5]=color[21];
            color[21]=temp;

            temp=color[0];
            color[0]=color[16];
            color[16]=color[4];
            color[4]=color[20];
            color[20]=temp;
        }


        bool solved() {
            char first;
            for (int i=0; i<6; i++) {
                first=color[4*i];
                for (int j=1; j<4; j++) {
                    if (color[4*i+j]!=first) {
                        return false;
                    }
                }
            }
            return true;
        }

        string solve() {
            string s=getMoves();
            
            string s2="";
            char col=color[0];
            int cnt=0;
            if (s=="") {
                return "";
            }
            for (int i=0; i<s.length(); i++) {
                if (s[i]==col) {
                    cnt++;
                } 
                else {
                    switch (cnt) {
                        case 1:
                            s2+=col;
                            s2+=' ';
                            break;
                        case 2:
                            s2+=col;
                            s2+="2 ";
                            break;
                        case 3:
                            s2+=col;
                            s2+="' ";
                            break;
                    }
                    col=s[i];
                    cnt=1;
                }
            }
            switch (cnt) {
                case 1:
                    s2+=col;
                    s2+=' ';
                    break;
                case 2:
                    s2+=col;
                    s2+="2 ";
                    break;
                case 3:
                    s2+=col;
                    s2+="' ";
                    break;
                default:
                    s2+=" ";
                    break;
            }
            return s2;
        }

        string getMoves() {
            if (solved()) {
                return "";
            }
            
            string original = color;
            string moves1 = "";
            string list1 = "";
            string moves2 = "";
            string list2 = "";
            string prevMove = "";
            int moveLen = 0;

            for (int move=0; move<3; move++) {
                color=original;
                switch (move) {
                    case 0 :
                        F();
                        if (solved()) {return "F";}
                        list1 += color;
                        moves1 += "F";
                        break;
                    case 1 :
                        U();
                        if (solved()) {return "U";}
                        list1 += color;
                        moves1 += "U";
                        break;
                    case 2 :
                        R();
                        if (solved()) {return "R";}
                        list1 += color;
                        moves1 += "R";
                        break;
                }
            }
            moveLen++;
            
            while (true) {
                moves2 = "";
                list2="";
                for (int cnt=0; cnt<list1.size()/24; cnt++) {
                    for (int move=0; move<3; move++) {
                        color=list1.substr(24*cnt,24);
                        prevMove=moves1.substr(moveLen*cnt,moveLen);
                        switch (move) {
                            case 0 :
                                F();
                                if (solved()) {return prevMove+"F";}
                                list2 += color;
                                moves2 += prevMove+"F";
                                break;
                            case 1 :
                                U();
                                if (solved()) {return prevMove+"U";}
                                list2 += color;
                                moves2 += prevMove+"U";
                                break;
                            case 2 :
                                R();
                                if (solved()) {return prevMove+"R";}
                                list2 += color;
                                moves2 += prevMove+"R";
                                break;
                        }
                    }
                }
                moveLen++;

                moves1 = "";
                list1 = "";
                for (int cnt=0; cnt<list2.size()/24; cnt++) {
                    for (int move=0; move<3; move++) {
                        color=list2.substr(24*cnt,24);
                        prevMove=moves2.substr(moveLen*cnt,moveLen);
                        switch (move) {
                            case 0 :
                                F();
                                if (solved()) {return prevMove+"F";}
                                list1 += color;
                                moves1 += prevMove+"F";
                                break;
                            case 1 :
                                U();
                                if (solved()) {return prevMove+"U";}
                                list1 += color;
                                moves1 += prevMove+"U";
                                break;
                            case 2 :
                                R();
                                if (solved()) {return prevMove+"R";}
                                list1 += color;
                                moves1 += prevMove+"R";
                                break;
                        }
                    }
                }
                moveLen++;
            }        
        }

};

int main() {
    string color = "obbygyrgrwowowrwyoyrbbgg"; // R F2 R2 F U2 R F2 
    Rubik r(color);

    string s=r.solve();

    cout << s << endl;
    return 0;
}