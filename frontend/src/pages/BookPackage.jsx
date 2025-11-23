import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { packageAPI, bookingAPI } from '../utils/api';

const BookPackage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [travelPackage, setTravelPackage] = useState(null); // Changed from 'package' to 'travelPackage'
  const [loading, setLoading] = useState(true);
  const [booking, setBooking] = useState({
    travellers: 1
  });
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchPackage();
  }, [id]);

  const fetchPackage = async () => {
    try {
      const response = await packageAPI.getById(id);
      setTravelPackage(response.data); // Updated here
    } catch (err) {
      setError('Package not found');
    } finally {
      setLoading(false);
    }
  };

  const handleTravellersChange = (e) => {
    const travellers = parseInt(e.target.value);
    setBooking({ travellers });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const user = JSON.parse(localStorage.getItem('user'));
    if (!user) {
      navigate('/login');
      return;
    }

    setSubmitting(true);
    setError('');

    try {
      await bookingAPI.create({
        package_id: parseInt(id),
        travellers: booking.travellers
      });
      
      alert('Booking successful!');
      navigate('/packages');
    } catch (err) {
      setError(err.response?.data?.error || 'Booking failed');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-4xl mx-auto px-4">
          <div className="text-center">Loading package details...</div>
        </div>
      </div>
    );
  }

  if (!travelPackage) { // Updated here
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-4xl mx-auto px-4">
          <div className="text-center text-red-600">Package not found</div>
        </div>
      </div>
    );
  }

  const totalPrice = travelPackage.price * booking.travellers; // Updated here

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4">
        <h1 className="text-3xl font-bold text-gray-800 mb-8">Book Your Package</h1>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            {error}
          </div>
        )}

        <div className="grid md:grid-cols-2 gap-8">
          {/* Package Details */}
          <div className="card p-6">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">{travelPackage.package_name}</h2> {/* Updated here */}
            <div className="space-y-3">
              <p><strong>Destination:</strong> {travelPackage.destination}</p> {/* Updated here */}
              <p><strong>Price per person:</strong> ${travelPackage.price}</p> {/* Updated here */}
              <p><strong>Description:</strong> {travelPackage.description}</p> {/* Updated here */}
            </div>
          </div>

          {/* Booking Form */}
          <div className="card p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4">Booking Details</h3>
            
            <form onSubmit={handleSubmit}>
              <div className="mb-6">
                <label htmlFor="travellers" className="block text-sm font-medium text-gray-700 mb-2">
                  Number of Travellers
                </label>
                <select
                  id="travellers"
                  name="travellers"
                  value={booking.travellers}
                  onChange={handleTravellersChange}
                  className="input-field"
                >
                  {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map(num => (
                    <option key={num} value={num}>{num}</option>
                  ))}
                </select>
              </div>

              <div className="bg-gray-50 p-4 rounded-lg mb-6">
                <div className="flex justify-between items-center mb-2">
                  <span>Price per person:</span>
                  <span>${travelPackage.price}</span> {/* Updated here */}
                </div>
                <div className="flex justify-between items-center mb-2">
                  <span>Number of travellers:</span>
                  <span>{booking.travellers}</span>
                </div>
                <div className="flex justify-between items-center text-lg font-bold border-t pt-2">
                  <span>Total Price:</span>
                  <span className="text-primary-600">${totalPrice}</span>
                </div>
              </div>

              <button
                type="submit"
                disabled={submitting}
                className="btn-primary w-full py-3"
              >
                {submitting ? 'Processing...' : 'Confirm Booking'}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookPackage;