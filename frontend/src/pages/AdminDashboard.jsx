import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { packageAPI, bookingAPI } from '../utils/api';
import PackageCard from '../components/PackageCard';

const AdminDashboard = () => {
  const [activeTab, setActiveTab] = useState('packages');
  const [packages, setPackages] = useState([]);
  const [bookings, setBookings] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [newPackage, setNewPackage] = useState({
    package_name: '',
    destination: '',
    price: '',
    description: ''
  });
  const navigate = useNavigate();

  useEffect(() => {
    const user = JSON.parse(localStorage.getItem('user'));
    if (!user || !user.is_admin) {
      navigate('/login');
      return;
    }

    if (activeTab === 'packages') {
      fetchPackages();
    } else if (activeTab === 'bookings') {
      fetchBookings();
    }
  }, [activeTab, navigate]);

  const fetchPackages = async () => {
    try {
      setLoading(true);
      const response = await packageAPI.getAll();
      setPackages(response.data);
    } catch (err) {
      setError('Failed to fetch packages');
    } finally {
      setLoading(false);
    }
  };

  const fetchBookings = async () => {
    try {
      setLoading(true);
      const response = await bookingAPI.getAll();
      setBookings(response.data);
    } catch (err) {
      setError('Failed to fetch bookings');
    } finally {
      setLoading(false);
    }
  };

  const handlePackageSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      await packageAPI.create({
        ...newPackage,
        price: parseFloat(newPackage.price)
      });
      
      setNewPackage({
        package_name: '',
        destination: '',
        price: '',
        description: ''
      });
      
      fetchPackages();
      alert('Package created successfully!');
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to create package');
    }
  };

  const handleInputChange = (e) => {
    setNewPackage({
      ...newPackage,
      [e.target.name]: e.target.value
    });
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-7xl mx-auto px-4">
          <div className="text-center">Loading...</div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4">
        <h1 className="text-3xl font-bold text-gray-800 mb-8">Admin Dashboard</h1>

        {/* Tabs */}
        <div className="border-b border-gray-200 mb-8">
          <nav className="-mb-px flex space-x-8">
            <button
              onClick={() => setActiveTab('packages')}
              className={`py-2 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'packages'
                  ? 'border-primary-500 text-primary-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              Manage Packages
            </button>
            <button
              onClick={() => setActiveTab('bookings')}
              className={`py-2 px-1 border-b-2 font-medium text-sm ${
                activeTab === 'bookings'
                  ? 'border-primary-500 text-primary-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              View Bookings
            </button>
          </nav>
        </div>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            {error}
          </div>
        )}

        {/* Packages Tab */}
        {activeTab === 'packages' && (
          <div className="space-y-8">
            {/* Add Package Form */}
            <div className="card p-6">
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Add New Package</h2>
              <form onSubmit={handlePackageSubmit} className="grid md:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Package Name
                  </label>
                  <input
                    type="text"
                    name="package_name"
                    value={newPackage.package_name}
                    onChange={handleInputChange}
                    required
                    className="input-field"
                    placeholder="e.g., Beach Paradise"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Destination
                  </label>
                  <input
                    type="text"
                    name="destination"
                    value={newPackage.destination}
                    onChange={handleInputChange}
                    required
                    className="input-field"
                    placeholder="e.g., Maldives"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Price
                  </label>
                  <input
                    type="number"
                    name="price"
                    value={newPackage.price}
                    onChange={handleInputChange}
                    required
                    step="0.01"
                    min="0"
                    className="input-field"
                    placeholder="e.g., 1200.00"
                  />
                </div>
                
                <div className="md:col-span-2">
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Description
                  </label>
                  <textarea
                    name="description"
                    value={newPackage.description}
                    onChange={handleInputChange}
                    rows="3"
                    className="input-field"
                    placeholder="Package description..."
                  />
                </div>
                
                <div className="md:col-span-2">
                  <button type="submit" className="btn-primary">
                    Add Package
                  </button>
                </div>
              </form>
            </div>

            {/* Packages List */}
            <div>
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Existing Packages</h2>
              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                {packages.map((pkg) => (
                  <PackageCard key={pkg.package_id} package={pkg} showBookButton={false} />
                ))}
              </div>
              
              {packages.length === 0 && (
                <div className="text-center text-gray-500 py-8">
                  No packages available. Add your first package above.
                </div>
              )}
            </div>
          </div>
        )}

        {/* Bookings Tab */}
        {activeTab === 'bookings' && (
          <div>
            <h2 className="text-2xl font-bold text-gray-800 mb-4">All Bookings</h2>
            
            {bookings.length === 0 ? (
              <div className="text-center text-gray-500 py-8">
                No bookings found.
              </div>
            ) : (
              <div className="card overflow-hidden">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Booking ID
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Customer
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Package
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Travellers
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Total Price
                      </th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {bookings.map((booking) => (
                      <tr key={booking.booking_id}>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                          #{booking.booking_id}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <div className="text-sm text-gray-900">{booking.customer_name}</div>
                          <div className="text-sm text-gray-500">{booking.email}</div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <div className="text-sm text-gray-900">{booking.package_name}</div>
                          <div className="text-sm text-gray-500">{booking.destination}</div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                          {booking.travellers}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                          ${booking.total_price}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default AdminDashboard;