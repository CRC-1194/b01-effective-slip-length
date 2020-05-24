Karman transformations[1]
$$ \xi = z\sqrt{\frac{\Omega}{\nu}}\qquad\qquad\qquad\qquad\qquad \qquad\qquad\qquad\quad\quad(1)$$
$$ u = \Omega rf^{'}(\xi) \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad (2)$$
$$ v = \Omega rg(\xi) \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad (3)$$
$$ w = -2\sqrt{\Omega \nu}f(\xi) \qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad\quad (4)$$
thus navier-stikes equations are reduced to
$$ F(\xi) = f^{'''}+2ff^{''}-(f^{'})^2+g^2 = 0 \qquad\qquad\qquad\qquad\quad (5)$$
$$ G(\xi) = g^{''}-2f^{'}g+2g^{'}f=0 \qquad\qquad\qquad\qquad\qquad\qquad (6)$$
with the following 10 boundary conditions
$$ f(0) = 0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (7)$$
$$ f^{'}(0) = 0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (8)$$
$$ g(0) = 0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (9)$$
$$ F(0) = 0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (10)$$
$$ G(0) = 0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (11)$$
$$ f(\xi_{h}) = 0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (12)$$
$$ f^{'}(\xi_{h}) = 0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (13)$$
$$ g(\xi_{h}) = 1 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (14)$$
$$ F(\xi_{h}) = 0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (15)$$
$$ G(\xi_{h}) = 0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad (16) $$
where 
$$ \xi_{h} = h\sqrt{\frac{\Omega}{\nu}} \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad (17)$$
where $h$ is the height of the wedge.
Suppose that
$$ f(\xi) = a_{1}\xi^6+a_{2}\xi^5+a_{3}\xi^4+a_{4}\xi^3+a_{5}\xi+a_{6} \qquad\qquad\qquad (18) $$
$$ g(\xi) =b_{1}\xi^4+b_{2}\xi^3+b_{3}\xi^2+b_{4} \qquad\qquad\qquad\qquad\qquad\quad (19) $$
Due to the 10 boundary conditions there can be maximal 10 coefficients, which can be assigned to the two functions. Here is one of the possibilities, which is found to fit the cfd-results relatively best.
With (7) - (16) can be solved and expressed as 
$$ f(\xi) = -\frac{1}{24}(\frac{\xi^6}{\xi^2_{h}}-2\frac{\xi^5}{\xi_{h}}+\xi^4) \qquad\qquad\qquad\quad\qquad\qquad\quad (20)$$
$$ g(\xi) = -\frac{\xi^4}{\xi^4_{h}}+2\frac{\xi^3}{\xi^3_{h}} \qquad\qquad\qquad\quad\qquad\qquad\qquad\qquad\quad (21)$$
Therefore the components of the velocity can be written as
$$ u(z) = -\frac{r}{12}\sqrt{\frac{\Omega^5}{\nu^3}}(3\frac{z^5}{h^3}-5\frac{z^4}{h^2}+2\frac{z^3}{h}) \qquad\qquad\qquad\quad\quad (22)$$
$$ v(z) = -\Omega r(\frac{z^4}{h^4}-2\frac{z^3}{h^3}) \qquad\qquad\qquad\qquad\qquad\qquad\quad\quad (23)$$
$$ w(z) = \frac{\Omega^2}{12\nu}(\frac{z^6}{h^3}-2\frac{z^5}{h^2}+\frac{z^4}{5}) \qquad\qquad\qquad\qquad\qquad\quad (24) $$
$$$$
References $$$$
[1] C.Y.WANG. Exact solutions of the steady-state navier-stokes equations, 1991.


