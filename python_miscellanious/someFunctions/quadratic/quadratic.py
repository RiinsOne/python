from quadratic_equation.utils import get_parameter, QuadraticEquation


def main():
    a = get_parameter('a')
    b = get_parameter('b')
    c = get_parameter('c')

    qe = QuadraticEquation(a, b, c)
    qe.calc_descr()

    if qe.get_desc() < 0:
        print('No results!')
    else:
        x1 = qe.calc_root()
        x2 = qe.calc_root(order=2)
        print(f'Results: x1={x1}, x2={x2}')


if __name__ == '__main__':
    main()


#
