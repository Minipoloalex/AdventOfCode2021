#ifndef INC_2021_DAY_15_POSITION_H
#define INC_2021_DAY_15_POSITION_H

#include <ostream>

#include "types.h"

class Position {
private:
    uint x;
    uint y;
    uint dist;
    int queueIndex = 0;
public:
    Position(uint x, uint y, uint dist);
    [[nodiscard]] uint getX() const;
    [[nodiscard]] uint getY() const;
    [[nodiscard]] uint getDist() const;
    void setDist(uint _dist);
    bool operator<(const Position &other) const;
    friend std::ostream& operator<<(std::ostream &out, const Position &position);
    friend class MutablePriorityQueue;
};


#endif //INC_2021_DAY_15_POSITION_H
