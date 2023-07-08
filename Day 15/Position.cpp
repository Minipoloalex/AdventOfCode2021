#include "Position.h"

Position::Position(uint x, uint y, uint dist): x(x), y(y), dist(dist) {}

uint Position::getX() const {
    return x;
}

uint Position::getY() const {
    return y;
}

bool Position::operator<(const Position &other) const {
    return this->dist < other.dist;
}

void Position::setDist(uint _dist) {
    this->dist = _dist;
}

uint Position::getDist() const {
    return this->dist;
}
std::ostream& operator<<(std::ostream &out, const Position &position) {
    out << "(" << position.x << "," << position.y << "," << position.dist << ")";
    return out;
}
