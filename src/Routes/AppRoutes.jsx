import { Routes, Route } from "react-router-dom";


function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Inicio/>} />
    </Routes>
  );
}

export default AppRoutes;
