#include iostream
#include string
#include string.h
#include vector
using namespace std;

int main()
{
    string input;
    getline(cin, input);
    string a = !@#$%^&()_++`1234567890-=={}qwertyuiop[]asdfghjkl;''zxcvbnm,.;
    int len = input.size();
    int lena = a.size();
    for (int i = 0; i  len; i++) {
        input[i] = tolower(input[i]);
    }
    for (int i = 0; i  len; i++) {
        for (int j = 0; j  lena; j++) {
            if (input[i] == ' ') {
                input[i] = ' ';
                break;
            }
            else if(input[i]==a[j])
            {
                input[i] = a[j + 1];
                break;
            }
        }
        cout  input[i];
    }
    cout  endl;
    return 0;
}