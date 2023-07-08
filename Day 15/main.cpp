#include <iostream>
#include <fstream>
#include <climits>
#include <queue>
#include <set>

#include "Position.h"
#include "MutablePriorityQueue.h"

using namespace std;

#define INF_UINT UINT_MAX

bool read_file(const string &input_file, matrix &m) {
    ifstream in(input_file);
    if (!in) {
        return false;
    }
    string line;
    while (getline(in, line)) {
        matrix_line vector_line;
        for (char c: line) {
            vector_line.push_back(c - '0');
        }
        m.push_back(vector_line);
    }
    return true;
}
template <class T>
void print_matrix(const vector<vector<T>> &m) {
    for (const vector<T> &line: m) {
        cout << "[ ";
        for (T value: line) {
            cout << value << " ";
        }
        cout << "]\n";
    }
}

void part_one() {
    matrix m;
    string input_file = "input.txt";
    if (!read_file(input_file, m)) {
        cout << "Could not find file " << input_file << endl;
    }

    uint rows = m.size();
    if (m.empty()) return;
    uint cols = m[0].size();

    matrix visited(rows, matrix_line(cols, false));

    MutablePriorityQueue pq;
    vector<vector<Position>> all_positions;
    for (uint y = 0; y < rows; y++) {
        vector<Position> line_positions;
        for (uint x = 0; x < cols; x++) {
            line_positions.emplace_back(x, y, INF_UINT);
        }
        all_positions.push_back(line_positions);
    }
    all_positions[0][0].setDist(0);
    pq.insert(&all_positions[0][0]);
    visited[0][0] = true;

    pair<uint, uint> next_positions[] = {make_pair(0, 1), make_pair(0, -1), make_pair(1, 0), make_pair(-1, 0)};
    while (!pq.empty()) {
        Position *position = pq.extractMin();
        for (const pair<uint, uint> &next_position : next_positions) {
            int newX = position->getX() + next_position.first;
            int newY = position->getY() + next_position.second;
            if (newX < 0 || newX >= cols || newY < 0 || newY >= rows) {
                continue;
            }
            Position &next = all_positions[newY][newX];
            uint oldDist = next.getDist();
            uint newDist = position->getDist() + m[newY][newX];
            if (newDist < oldDist) {
                next.setDist(newDist);
                if (visited[newY][newX]) {
                    pq.decreaseKey(position);
                }
                else {
                    visited[newY][newX] = true;
                    pq.insert(&next);
                }
            }
        }
    }
    // print_matrix(all_positions);
    cout << all_positions[rows - 1][cols - 1] << endl;
}


class PartTwo {
private:
    uint get_value(uint x, uint y, uint rows, uint cols, const matrix &values) {
        int cell_row = y/rows;  // starts from 0, up to 4
        int cell_col = x/cols;  // starts from 0, up to 4

        // get the corresponding value in our cell
        uint corresponding_value = values[y - cell_row * rows][x - cell_col * cols];

        uint return_value = corresponding_value + cell_row + cell_col;
        return return_value > 9 ? return_value - 9 : return_value;
    }
public:
    void execute() {
        matrix m;
        string input_file = "input.txt";
        if (!read_file(input_file, m)) {
            cout << "Could not find file " << input_file << endl;
        }

        uint rows = m.size();
        if (m.empty()) return;
        uint cols = m[0].size();

        uint all_rows = rows * 5;
        uint all_cols = cols * 5;

        matrix visited(all_rows, matrix_line(all_cols, false));

        MutablePriorityQueue pq;
        vector<vector<Position>> all_positions;
        for (uint y = 0; y < all_rows; y++) {
            vector<Position> line_positions;
            for (uint x = 0; x < all_cols; x++) {
                line_positions.emplace_back(x, y, INF_UINT);
            }
            all_positions.push_back(line_positions);
        }
        all_positions[0][0].setDist(0);
        pq.insert(&all_positions[0][0]);
        visited[0][0] = true;

        pair<uint, uint> next_positions[] = {make_pair(0, 1), make_pair(0, -1), make_pair(1, 0), make_pair(-1, 0)};
        while (!pq.empty()) {
            Position *position = pq.extractMin();
            for (const pair<uint, uint> &next_position : next_positions) {
                int newX = position->getX() + next_position.first;
                int newY = position->getY() + next_position.second;
                if (newX < 0 || newX >= all_cols || newY < 0 || newY >= all_rows) {
                    continue;
                }
                Position &next = all_positions[newY][newX];
                uint oldDist = next.getDist();
                uint newDist = position->getDist() + get_value(newX, newY, rows, cols, m);
                if (newDist < oldDist) {
                    next.setDist(newDist);
                    if (visited[newY][newX]) {
                        pq.decreaseKey(position);
                    }
                    else {
                        visited[newY][newX] = true;
                        pq.insert(&next);
                    }
                }
            }
        }
        // print_matrix(all_positions);
        cout << all_positions[all_rows - 1][all_cols - 1] << endl;
    }
};

int main() {
    PartTwo partTwo;
    partTwo.execute();
    return 0;
}
