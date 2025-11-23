import React from 'react';
import { Link } from 'react-router-dom';

const PackageCard = ({ package: pkg, showBookButton = true }) => {
  return (
    <div className="card hover:shadow-lg transition duration-300">
      <div className="h-48 bg-gradient-to-r from-primary-500 to-primary-600 flex items-center justify-center">
        <span className="text-white text-2xl font-bold">{pkg.destination}</span>
      </div>
      
      <div className="p-6">
        <h3 className="text-xl font-bold text-gray-800 mb-2">{pkg.package_name}</h3>
        <p className="text-gray-600 mb-4 line-clamp-2">{pkg.description}</p>
        
        <div className="flex justify-between items-center mb-4">
          <span className="text-2xl font-bold text-primary-600">
            ${pkg.price}
          </span>
          <span className="text-sm text-gray-500">per person</span>
        </div>

        {showBookButton && (
          <div className="flex space-x-2">
            <Link
              to={`/book/${pkg.package_id}`}
              className="btn-primary flex-1 text-center"
            >
              Book Now
            </Link>
          </div>
        )}
      </div>
    </div>
  );
};

export default PackageCard;