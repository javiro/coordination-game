/*
 * Game.cpp
 *
 *  Created on: 22 feb. 2020
 *      Author: javi
 */

#include "Game.h"

double TransitionMatrix::q() {
  return length_ * length_ * length_;
}

double TransitionMatrix::p() {
  return 6 * length_ * length_;
}

double TransitionMatrix::getTransitionMatrix() {
  return 6 * length_ * length_;
}

double TransitionMatrix::getStateTickK() {
  return 6 * length_ * length_;
}

void TransitionMatrix::plotMeanDynamics() {
  return 6 * length_ * length_;
}

void TransitionMatrix::plotStates(double length) {
  length_ = length;
}


