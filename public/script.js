document.addEventListener('DOMContentLoaded', () => {
  const apiUrl = '/api/data';

  // State names
  const reversed_state_abbr_map = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District of Columbia",
    "FM": "Federated States of Micronesia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "PW": "Republic of Palau",
    "MH": "Republic of the Marshall Islands",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VI": "Virgin Islands",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
  };

  // Load JSON data
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      const pageType = document.body.id; // Identify the page type (overview or state)
      if (pageType === 'index') renderStatesTable(data);
      else if (pageType === 'state') renderDistrictsTable(data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });

  // Render states overview table
  function renderStatesTable(data) {
    const tableBody = document.getElementById('statesTable').querySelector('tbody');
    Object.keys(data).forEach((stateId) => {
      const state = data[stateId];
      const stateRow = `
        <tr>
          <td>${reversed_state_abbr_map[state["state_abbr"]]}</td>
          <td><a href="${state['yt-link'] || '#'}" target="_blank">YouTube</a></td>
          <td><a href="${state.website || '#'}" target="_blank">Website</a></td>
          <td><a href="state.html?state=${stateId}">Districts</a></td>
          <td>${Object.keys(state.districts).length}</td>
        </tr>
      `;
      tableBody.insertAdjacentHTML('beforeend', stateRow);
    });
  }

  // Render districts table for a specific state
  function renderDistrictsTable(data) {
    const urlParams = new URLSearchParams(window.location.search);
    const stateId = urlParams.get('state');
    const state = data[stateId];
    document.getElementById('stateName').textContent = `Districts in ${stateId}`;

    const tableBody = document.getElementById('districtsTable').querySelector('tbody');
    Object.keys(state.districts).forEach((districtId) => {
      const district = state.districts[districtId];
      const districtRow = `
        <tr>
          <td>${districtId}</td>
          <td>BLANK</td>
          <td>BLANK</td>
        </tr>
      `;
      tableBody.insertAdjacentHTML('beforeend', districtRow);
    });
  }
});