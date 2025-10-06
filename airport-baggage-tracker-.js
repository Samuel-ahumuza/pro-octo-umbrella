// A simulated database of movies
const movies = [
    {
        id: 'movie1',
        title: 'Mission: Impossible - Dead Reckoning Part One',
        poster: 'https://m.media-amazon.com/images/M/MV5BNTIxYWJmOWEtYzg0Yi00MzZiLTg4MzMtZmQ4ZDE2OTJkNzM1XkEyXkFqcGdeQXVyMTE0MTY2MDUw._V1_FMjpg_UX1000_.jpg',
        summary: 'Ethan Hunt and his IMF team embark on their most dangerous mission yet: to track a terrifying new weapon that threatens all of humanity before it falls into the wrong hands.',
        rating: '8.0',
        showtimes: [
            { id: 't1', time: '10:00 AM', day: 'Monday' },
            { id: 't2', time: '1:30 PM', day: 'Tuesday' },
            { id: 't3', time: '7:00 PM', day: 'Thursday' }
        ],
        bookedSeats: ['A1', 'A2', 'B5']
    },
    {
        id: 'movie2',
        title: 'Oppenheimer',
        poster: 'https://m.media-amazon.com/images/M/MV5BMDBmYTrFj2QtNzMzMS00NDRkLTgwYmEtZjI2MjcwNzkxZmI2XkEyXkFqcGdeQXVyMTE1MjMyMjcx._V1_FMjpg_UX1000_.jpg',
        summary: 'The story of J. Robert Oppenheimer, the scientist who led the effort to develop the atomic bomb during World War II.',
        rating: '8.6',
        showtimes: [
            { id: 't4', time: '11:00 AM', day: 'Monday' },
            { id: 't5', time: '4:00 PM', day: 'Wednesday' },
            { id: 't6', time: '8:00 PM', day: 'Friday' }
        ],
        bookedSeats: ['C3', 'C4', 'C5', 'F8']
    }
];

// Get references to HTML elements
const scheduleGrid = document.getElementById('schedule-grid');
const scheduleView = document.getElementById('schedule-view');
const movieDetailsView = document.getElementById('movie-details');
const bookingView = document.getElementById('booking-view');
const backToScheduleBtn = document.getElementById('back-to-schedule');
const seatingChart = document.getElementById('seating-chart');
const selectedSeatsCount = document.getElementById('selected-seats-count');
const totalPriceDisplay = document.getElementById('total-price');
const confirmBookingBtn = document.getElementById('confirm-booking');

let selectedSeats = [];
const TICKET_PRICE = 10.00;
let currentMovieData = null;
let currentShowtimeData = null;

// Function to render the movie schedule
function renderSchedule() {
    scheduleGrid.innerHTML = ''; // Clear previous content
    movies.forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.className = 'movie-card';
        movieCard.dataset.movieId = movie.id;
        movieCard.innerHTML = `
            <img src="${movie.poster}" alt="${movie.title}">
            <div class="card-content">
                <h3>${movie.title}</h3>
                <p><strong>Rating:</strong> ${movie.rating}</p>
            </div>
        `;
        movieCard.addEventListener('click', () => showMovieDetails(movie.id));
        scheduleGrid.appendChild(movieCard);
    });
}

// Function to show the movie details page
function showMovieDetails(movieId) {
    const movie = movies.find(m => m.id === movieId);
    currentMovieData = movie;
    if (movie) {
        document.getElementById('movie-poster').src = movie.poster;
        document.getElementById('movie-title').textContent = movie.title;
        document.getElementById('movie-summary').textContent = movie.summary;
        document.getElementById('movie-rating').textContent = movie.rating;
        
        const showtimeOptions = document.getElementById('showtime-options');
        showtimeOptions.innerHTML = '';
        movie.showtimes.forEach(showtime => {
            const btn = document.createElement('button');
            btn.className = 'showtime-btn';
            btn.textContent = `${showtime.day}, ${showtime.time}`;
            btn.addEventListener('click', () => showBookingView(movie, showtime));
            showtimeOptions.appendChild(btn);
        });

        scheduleView.classList.add('hidden');
        movieDetailsView.classList.remove('hidden');
    }
}

// Function to show the seat booking page
function showBookingView(movie, showtime) {
    currentShowtimeData = showtime;
    selectedSeats = [];
    updateBookingSummary();
    
    document.getElementById('booking-title').textContent = `${movie.title} - ${showtime.day}, ${showtime.time}`;
    seatingChart.innerHTML = '';
    const totalSeats = 50; // Example total seats
    const bookedSeats = movie.bookedSeats;

    for (let i = 1; i <= totalSeats; i++) {
        const seat = document.createElement('div');
        seat.className = 'seat';
        seat.textContent = i;
        const seatNumber = getSeatNumber(i);
        seat.dataset.seatNumber = seatNumber;

        if (bookedSeats.includes(seatNumber)) {
            seat.classList.add('booked');
        } else {
            seat.addEventListener('click', () => toggleSeat(seat));
        }
        seatingChart.appendChild(seat);
    }
    
    movieDetailsView.classList.add('hidden');
    bookingView.classList.remove('hidden');
}

// Helper function to create a seat number like A1, B2 etc
function getSeatNumber(index) {
    const row = String.fromCharCode(65 + Math.floor((index - 1) / 10));
    const col = (index - 1) % 10 + 1;
    return `${row}${col}`;
}

// Function to toggle seat selection
function toggleSeat(seat) {
    const seatNumber = seat.dataset.seatNumber;
    if (seat.classList.contains('selected')) {
        seat.classList.remove('selected');
        selectedSeats = selectedSeats.filter(s => s !== seatNumber);
    } else {
        seat.classList.add('selected');
        selectedSeats.push(seatNumber);
    }
    updateBookingSummary();
}

// Function to update the booking summary
function updateBookingSummary() {
    selectedSeatsCount.textContent = selectedSeats.length;
    const totalPrice = selectedSeats.length * TICKET_PRICE;
    totalPriceDisplay.textContent = totalPrice.toFixed(2);

    if (selectedSeats.length > 0) {
        confirmBookingBtn.classList.remove('disabled');
    } else {
        confirmBookingBtn.classList.add('disabled');
    }
}

// Function to handle booking confirmation
function handleBooking() {
    if (selectedSeats.length === 0) {
        alert('Please select at least one seat.');
        return;
    }

    const bookingInfo = {
        movie: currentMovieData.title,
        showtime: currentShowtimeData.time,
        seats: selectedSeats
    };

    console.log('Booking confirmed:', bookingInfo);
    alert(`Booking confirmed for ${bookingInfo.movie}! You have booked seats: ${bookingInfo.seats.join(', ')}`);
    
    // You could save this booking info to a database here
    
    // Go back to the schedule view
    bookingView.classList.add('hidden');
    scheduleView.classList.remove('hidden');
    selectedSeats = [];
}

// Event Listeners
backToScheduleBtn.addEventListener('click', () => {
    movieDetailsView.classList.add('hidden');
    scheduleView.classList.remove('hidden');
});
confirmBookingBtn.addEventListener('click', handleBooking);

// Initial call to render the schedule when the page loads
document.addEventListener('DOMContentLoaded', renderSchedule);
