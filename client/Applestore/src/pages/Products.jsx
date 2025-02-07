import { useEffect, useState } from "react";
import axios from "axios";
import ProductList from "../components/ProductList";
import CreateProductForm from "../components/CreateProductForm";

function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get("https://applestore-cdyy.onrender.com/products")
      .then(response => setProducts(response.data))
      .catch(error => console.error("Error fetching products:", error));
  }, []);

  return (
    <div>
      <h2>Products</h2>
      <CreateProductForm setProducts={setProducts} />
      <ProductList products={products} setProducts={setProducts} />
    </div>
  );
}

export default Products;
