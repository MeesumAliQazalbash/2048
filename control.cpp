// g++ *.cpp -I /usr/include/SDL2/ -lSDL2 -lSDL2_image -lSDL2_ttf -lSDL2_mixer

#include <control.hpp>

Grid::Grid() : n(5) { initialize(5); }

Grid::Grid(const int num) : n(num) { initialize(num); }

void Grid::getInput()
{
    char direction;
    twitch();
    if (terminate)
    {
        std::cout << "Game Ended" << std::endl;
    }
    else
    {
        show();
        std::cout << "Enter the direction: ";
        std::cin >> direction;
        shift(direction);
        getInput();
    }
}
void Grid::show()
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            std::cout << *(g + n * i + j) << "  ";
        }
        std::cout << std::endl;
    }
    std::cout << "\n\n"
              << std::endl;
}

void Grid::up()
{
    int factor, entry;
    for (int pCol = 0; pCol < n; pCol++)
    {
        q = {};
        for (int pRow = 0; pRow < n; pRow++)
        {
            entry = *(g + n * pRow + pCol);
            if (entry != 0)
            {
                factor = 1;
                if (q.size() && q.back() == entry)
                {
                    q.pop_back();
                    factor = 2;
                }
                q.push_back(entry * factor);
                terminate = entry * factor == 2048;
                *(g + n * pRow + pCol) = 0;
            }
        }
        int size = q.size();
        for (int i = 0; i < size; i++)
        {
            *(g + n * i + pCol) = q.back();
            q.pop_back();
        }
    }
}

void Grid::down()
{
    int factor, entry;
    for (int pCol = 0; pCol < n; pCol++)
    {
        q = {};
        for (int pRow = 0; pRow < n; pRow++)
        {
            entry = *(g + n * pRow + pCol);
            if (entry != 0)
            {
                factor = 1;
                if (q.size() && q.back() == entry)
                {
                    q.pop_back();
                    factor = 2;
                }
                q.push_back(entry * factor);
                terminate = entry * factor == 2048;
                *(g + n * pRow + pCol) = 0;
            }
        }
        int size = q.size();
        for (int i = n - 1; i > n - size - 1; i--)
        {
            *(g + n * i + pCol) = q.back();
            q.pop_back();
        }
    }
}

void Grid::left()
{
    int factor, entry;
    for (int pRow = 0; pRow < n; pRow++)
    {
        q = {};
        for (int pCol = 0; pCol < n; pCol++)
        {
            entry = *(g + n * pRow + pCol);
            if (entry != 0)
            {
                factor = 1;
                if (q.size() && q.back() == entry)
                {
                    q.pop_back();
                    factor = 2;
                }
                q.push_back(entry * factor);
                terminate = entry * factor == 2048;
                *(g + n * pRow + pCol) = 0;
            }
        }
        int size = q.size();
        for (int i = 0; i < size; i++)
        {
            *(g + n * pRow + i) = q.back();
            q.pop_back();
        }
    }
}

void Grid::right()
{
    int factor, entry;
    for (int pRow = 0; pRow < n; pRow++)
    {
        q = {};
        for (int pCol = 0; pCol < n; pCol++)
        {
            entry = *(g + n * pRow + pCol);
            if (entry != 0)
            {
                factor = 1;
                if (q.size() && q.back() == entry)
                {
                    q.pop_back();
                    factor = 2;
                }
                q.push_back(entry * factor);
                terminate = entry * factor == 2048;
                *(g + n * pRow + pCol) = 0;
            }
        }
        int size = q.size();
        for (int i = n - 1; i > n - size - 1; i--)
        {
            *(g + n * pRow + i) = q.back();
            q.pop_back();
        }
    }
}

void Grid::shift(char direction)
{
    if (direction == 'u' || direction == 'U')
    {
        up();
    }
    else if (direction == 'd' || direction == 'D')
    {
        down();
    }
    else if (direction == 'l' || direction == 'L')
    {
        left();
    }
    else if (direction == 'r' || direction == 'R')
    {
        right();
    }
    else
    {
        std::cout << "Unrecognized Input" << std::endl;
    }
}

void Grid::twitch()
{
    terminate = true;
    for (int p = 0; p < n * n; p++)
    {
        if (*(g + p) == 0 && rand() % (n - 1) == 0)
        {
            *(g + p) = 2;
            terminate = false;
            break;
        }
    }
}

void Grid::initialize(int num)
{
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
        {
            *(g + num * i + j) = 0;
        }
    }
    *(g + rand() % (n * n)) = 2;
    *(g + rand() % (n * n)) = 2;
}

int main()
{
    Grid c;

    c.getInput();

    return 0;
}