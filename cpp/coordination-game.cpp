
int main(int argc, char **argv) {

    m = TransitionMatrix(100)
    a0 = np.zeros(m.get_transition_matrix().shape[0])
    # a0[int((len(a0)-1) / 2)] = 1
    a0[40] = 1
    # m.plot_mean_dynamics(a0, 1000)
    m.plot_states(a0, [100, 200, 300, 400, 500])

	return 0;
}

#include <iostream>
#include "Cube.h"

int main() {

  TransitionMatrix m;

  c.number_of_players_(100);
  double volume = c.getVolume();
  std::cout << "Volume: " << volume << std::endl;

  return 0;
}
