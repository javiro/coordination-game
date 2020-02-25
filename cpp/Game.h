/*
 * Game.h
 *
 *  Created on: 22 feb. 2020
 *      Author: javi
 */

#ifndef GAME_H_
#define GAME_H_


// All header (.h) files start with "#pragma once":
#pragma once

// A class is defined with the `class` keyword, the name
// of the class, curly braces, and a required semicolon
// at the end:
class TransitionMatrix {
  public:  // Public members:
    double q();
    double p();
    double getTransitionMatrix();
    double getStateTickK();
    void plotMeanDynamics();
    void plotStates(double length);

  private: // Private members:
    int number_of_players_;
};


#endif /* GAME_H_ */
