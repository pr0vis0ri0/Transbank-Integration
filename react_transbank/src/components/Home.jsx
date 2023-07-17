const products = [
    { title: 'Frutilla', esFruta: true , id: 1},
    { title: 'Manzana', esFruta: true , id: 2},
    { title: 'Ajo', esFruta: false , id: 3},
];

export default function ListaDeCompras() {
    const itemsLista = products.map(product =>
            <li
                key={product.id}
                style= {{
                    color: product.esFruta ? 'magenta' : 'darkgreen'
                }}>
                {product.title}
            </li>
        );

    return (
        <ul>{itemsLista}</ul>
    );
}
  