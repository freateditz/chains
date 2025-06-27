import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Homepage from "./components/Homepage";
import FileFIR from "./pages/FileFIR";
import TrackStatus from "./pages/TrackStatus";
import Resources from "./pages/Resources";
import Contact from "./pages/Contact";
import CurrentCases from "./pages/CurrentCases";
import CitizenLogin from "./pages/CitizenLogin";
import AdminLogin from "./pages/AdminLogin";
import CitizenSignup from "./pages/CitizenSignup";
import AdminSignup from "./pages/AdminSignup";
import CitizenDashboard from "./pages/CitizenDashboard";
import AdminDashboard from "./pages/AdminDashboard";
import ProtectedRoute from "./components/ProtectedRoute";
import AuthGuard from "./components/AuthGuard";

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <BrowserRouter>
          <div className="flex flex-col min-h-screen">
            <Navbar />
            <main className="flex-grow">
              <Routes>
                <Route path="/" element={<Homepage />} />
                
                {/* Protected FIR Filing Route - Requires Citizen Login */}
                <Route 
                  path="/file-fir" 
                  element={
                    <ProtectedRoute requiredUserType="citizen">
                      <FileFIR />
                    </ProtectedRoute>
                  } 
                />
                
                {/* Protected Dashboard Routes */}
                <Route 
                  path="/citizen-dashboard" 
                  element={
                    <ProtectedRoute requiredUserType="citizen">
                      <CitizenDashboard />
                    </ProtectedRoute>
                  } 
                />
                <Route 
                  path="/admin-dashboard" 
                  element={
                    <ProtectedRoute requiredUserType="admin">
                      <AdminDashboard />
                    </ProtectedRoute>
                  } 
                />
                
                {/* Public Routes */}
                <Route path="/status" element={<TrackStatus />} />
                <Route path="/resources" element={<Resources />} />
                <Route path="/current-cases" element={<CurrentCases />} />
                <Route path="/contact" element={<Contact />} />
                
                {/* Auth Routes - Redirect to dashboard if already logged in */}
                <Route 
                  path="/citizen-login" 
                  element={
                    <AuthGuard requireAuth={false}>
                      <CitizenLogin />
                    </AuthGuard>
                  } 
                />
                <Route 
                  path="/admin-login" 
                  element={
                    <AuthGuard requireAuth={false}>
                      <AdminLogin />
                    </AuthGuard>
                  } 
                />
                <Route 
                  path="/citizen-signup" 
                  element={
                    <AuthGuard requireAuth={false}>
                      <CitizenSignup />
                    </AuthGuard>
                  } 
                />
                <Route 
                  path="/admin-signup" 
                  element={
                    <AuthGuard requireAuth={false}>
                      <AdminSignup />
                    </AuthGuard>
                  } 
                />
              </Routes>
            </main>
            <Footer />
          </div>
        </BrowserRouter>
      </AuthProvider>
    </div>
  );
}

export default App;