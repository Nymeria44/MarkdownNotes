==first-order== refers to the fact that the equations to describe the voltages and currents are first-order differential equations.

# The Natural Response
The ==natural response== of a circuit is the analysis of a circuit when the stored energy is allowed to dissipate. The methods used to analyse regular circuits such as KVL, KCL and so on are still used in solving the natural response but now they will lead to expressions that are functions of time.
An important rule to keep in mind when deriving the voltage and current expressions for the natural response of a circuit is that: 
- Current cannot change instantaneous across an inductor
- Voltage cannot change instantaneous across a capacitor

This is often mathematically represented as:
$$
i(0^-) = i(0^+)
$$
$$
v(0^-) = v(0^+)
$$

## The Time Constant
When solving the natural response of a circuit it is incredibly common to have a term such as, $e^{-(R/L)t}$.
The time constant is the terms used to describe the coefficient of $t$. It also indicates the rate at which the voltage or current within the circuit is approaching zero.

### Time Constant for $RL$
The time constant in an $RL$ circuit is:
$$
\tau = \frac{L}{R}
$$

### Time Constant for $RC$
The time constant in an $RC$ circuit is:
$$
\tau = RC
$$

## Equation of the $RL$ Natural Response
$$
i(t) = I_0 e^{-t/\tau}, \quad t \ge 0
$$
*Where $I_0$ is the current of the source*

## Equation of the $RC$ Natural Response
$$
v(t) = V_0 e^{-t/\tau},  \quad t \ge 0
$$
*Where $V_0$ is the voltage of the source*

# The Step Response
The ==step response== of a circuit refers to when a dc voltage or current source is applied. The equations describing it are inverse to those of the natural response in the sense they describe how over time the circuit reaches its steady state equilibrium.

## Equation of the $RL$ Step Response
$$
i(t) = \frac{V_s}{R} + (I_0 - \frac{V_s}{R})e^{-t/\tau}
$$
*Where $I_0$ is the initial current at $t = 0$.*


## Equation of the $RC$ Step Response
$$
v_C = I_s R + (V_0 - I_s R)e^{-t/\tau}
$$
*Where $I_0$ is the initial current at $t = 0$.*


# Methodology for determining Natural and Step Responses
- Determine if you are finding the current or the voltage
	- Commonly capacitive voltage is found for $RC$ circuits
	- Commonly inductive current in found for $RL$ circuits
- Determine any initial values for $t_0$.
- Find the steady state of the circuit by finding what happens when $t \rightarrow \infin$,
	- The steady state of a circuit is reached when the transients (natural and step responses) have completely decayed.
- Find the time constant of the circuit, $\tau$.
