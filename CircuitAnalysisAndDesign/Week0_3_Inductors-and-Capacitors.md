# Inductors
An inductor is a coiled wire that uses the magnetic field created by the coils to store energy.
The inductance of an inductor is denoted with the letter $L$ and has units of Henries `H`.

## Voltage and Current
The voltage across an inductor is:
$$
v = L \frac{di}{dt}
$$
The current through an inductor is:
$$
i(t) =  \frac{1}{L} \int_0^t v d\tau + i(t_0)
$$
*Where $i(t_0)$ represents the inital current through the inductor.*

## Power
Power across an inductor is:
$$
p = vi = Li \frac{di}{dt}
$$

# Capacitors
A capacitor is two metal plates with a dielectric or insulating material placed between them.
Capacitance is denoted with $C$ and is measured in farads `F`.

## Voltage and Current
The current through a capacitor can be calculated as follows:
$$
i = C \frac{dv}{dt}
$$
$$
v(t) =  \frac{1}{C} \int_0^t v d\tau + v(t_0)
$$

## Power
Power across an capacitor is:
$$
p = vi = Ci \frac{di}{dt}
$$

# Series-Parallel Relationship for Inductors and Capacitors
## Inductors
Inductors have the same behaviour as resistors, so in ==series==:
$$
L_{eq} = L_1 + L_2 + ... + L_n
$$
In ==parrallel==:
$$
\frac{1}{L_{eq}} = \frac{1}{L_1} +  \frac{1}{L_1} + ... +  \frac{1}{L_n}  
$$

## Capacitors
Capacitors are inverse to inductors, so in ==series==:
$$
\frac{1}{C_{eq}} = \frac{1}{C_1} +  \frac{1}{C_1} + ... +  \frac{1}{C_n}  
$$
In ==parrallel==:
$$
C_{eq} = C_1 + C_2 + ... + C_n
$$

# Mutual Inductance
Mutual inductance is when two circuits are linked to each other by a magnet field.
Mutual inductance is given the symbol $M$.
![Mutual-inductance-circuit-diagram.png](../../_resources/Mutual-inductance-circuit-diagram.png)

## Mutual Inductance Analysis
A common method used to analyse circuits with mutual inductance is through mesh analysis:
- Pick a direction for $i_1$ and $i_2$
- Sum voltages around the loop
- Across the coupled coils, there are two voltages of each coil
	- The "self-induced" voltage (normal inductor voltage), which is equal to $v_1 = L\frac{di_1}{dt}$
	- The second is the mutual inductance given by $v_1 = M\frac{di_2}{dt}$

## Sign Convention
To determine the polarity of the voltage induced by mutual inductance, the ==dot convention== is used:
- If a current enters the dot, then the voltage it induces in the other coil will be positive at the other dot.
- If the current leaves the dot, then the voltage it induces in the other will be negative at the dot.
*Both of these cases are illustrated in the circuit diagram of Mutual Inductance*

## Coupling Coefficient
The ==coupling coefficient== $k$, is a ratio that relates the self-inductance of the coil ($L_1, L_2$) to the mutual inductance $M$.
$$
M = k \sqrt{L_1 L_2}
$$
It is important to note that your value of k should always be:
$$
0 \ge k \ge 1
$$
