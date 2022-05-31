#include <iostream>
#include <vector>

class Grid
{
public:
    Grid();
    Grid(const int);
    void getInput();
    int *g = new int[n * n];

private:
    void show();
    void up();
    void down();
    void left();
    void right();
    void twitch();
    void shift(char);
    void initialize(int);
    const int n = 5;
    std::vector<int> q;
    bool terminate = false;
};