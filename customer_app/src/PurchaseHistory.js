import './PurchaseHistory.css';

function BuyList({buyList}) {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>User</th>
          <th>User ID</th>
          <th>Price</th>
          <th>Product</th>
          <th>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        {buyList.map((purchase, index) => (
          <tr key={index}>
            <td>{purchase.username}</td>
            <td>{purchase.user_id}</td>
            <td>${purchase.price.toFixed(2)}</td>
            <td>{purchase.product}</td>
            <td>{purchase.timestamp}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default BuyList;