window.onload = setHours;

let d = new Date();
let offset = d.getTimezoneOffset()/60;
let offsetDifference = offset - 6;

let month = d.getMonth() + 1;
let day = d.getDate();
let hours = d.getHours() + offsetDifference;
let minutes = d.getMinutes();
let minutesBeforeOpeningOrClosing = 60 - minutes;

let busHours;
let status;

// Concert List 2021 for easier hour mapping
let concerts = []

// #region CONCERT 'PUSH' OPERATIONS (HIDDEN)
concerts.push(new Date(2021, 07, 30));
concerts.push(new Date(2021, 08, 01));
concerts.push(new Date(2021, 08, 04));
concerts.push(new Date(2021, 08, 06));
concerts.push(new Date(2021, 08, 08));
concerts.push(new Date(2021, 08, 10));
concerts.push(new Date(2021, 08, 13));
concerts.push(new Date(2021, 08, 15));
concerts.push(new Date(2021, 08, 16));
concerts.push(new Date(2021, 08, 17));
concerts.push(new Date(2021, 08, 19));
concerts.push(new Date(2021, 08, 22));
concerts.push(new Date(2021, 08, 23));
concerts.push(new Date(2021, 08, 25));
concerts.push(new Date(2021, 08, 26));
concerts.push(new Date(2021, 08, 29));
concerts.push(new Date(2021, 09, 02));
concerts.push(new Date(2021, 09, 05));
concerts.push(new Date(2021, 09, 12));
concerts.push(new Date(2021, 09, 14));
concerts.push(new Date(2021, 09, 16));
concerts.push(new Date(2021, 09, 20));
concerts.push(new Date(2021, 09, 22));
concerts.push(new Date(2021, 09, 23));
concerts.push(new Date(2021, 09, 29));
concerts.push(new Date(2021, 09, 30));
//#endregion


//#region Constant Garden status variables and messages
const manualOverrideTrue = (document.getElementById('hours_override').textContent === 'True')

const daylightEndDay = 7;  // Day that Daylight Savings Time Ends in November of the current year
const daylightStartDay = 8;  // Day that Daylight Savings Time Begins in March of the next year

const thanksgivingDay = 25;  // Day of Month of Thanksgiving Holiday in November

const holidayPartyDay = parseInt(document.getElementById('hours_holiday_day').textContent);  // Day of Month we close for Holiday Party in December
const holidayPartyClosingHour = parseInt(document.getElementById('hours_holiday_hour').textContent);  // Hour we close on day of Holiday Party (military time)
const holidayPartyClosingMinute = parseInt(document.getElementById('hours_holiday_minute').textContent);  // Minute we close on day of Holiday Party (military time)

const galaMonth = 0;  // Month of Gala
const galaDay = 0;  // Day of month of Gala


/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
/* 		For MISC Messages that Appear in Status Divs								  */
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
const gardenOpenMessage = "<div style=\x22font-weight:bold;color:#49E20E;\x22>The Garden is Open</div>";
const gardenClosedMessage = "<div style=\x22color:red;font-weight:bold;\x22>The Garden is Closed Now</div>";
const gardenWillOpenMessageStart = "<div style=\x22font-weight:bold;color:#FF0000;\x22>The Garden Will Open in ";
const gardenWillCloseMessageStart = "<div style=\x22font-weight:bold;color:#FF0000;\x22>The Garden Will Close in ";
const gardenMessageEnd = " Minutes</div>";
const halfOffAdmission = "Enjoy half-price admission December, January, and February";
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
//#endregion


function setHours() {
	if (manualOverrideTrue) {
		const openHour = document.getElementById("hours_man_open").textContent;
		const closeHour = document.getElementById("hours_man_close").textContent;
		busHours = openHour + " &ndash; " + closeHour;
		// Check if hours_man_open and hours_man_close is actually set before setting the gardenHours content, otherwise we end up with just the '-'
		if (openHour && closeHour) {
			document.getElementById("gardenHours").innerHTML = busHours;
		}
		document.getElementById("gardenStatus").innerHTML = document.getElementById("hours_man_add_msg").textContent;
		document.getElementById("gardenEmphatic").innerHTML = document.getElementById("hours_man_add_emph_msg").textContent;
	} else {
		gardenYearlyHours();
	}
}


/**
 *  Sets concert day status; Returns true if it's a concert day
 **/
function isConcertDay(concerts, busHours) {
	didSetHours = false;

	// Loops through each concert to check if it's a concert day; Runs in O(N) time.
	concerts.forEach(concert => {
		if (concert.getMonth() == month && concert.getDate() == day) {
			document.getElementById("gardenHours").innerHTML = busHours;

			if (hours >= 9 && hours < 16) {
				status = gardenOpenMessage;
				document.getElementById("gardenStatus").innerHTML = status;
			}

			if (hours == 16) {
				status = gardenWillCloseMessageStart + minutesBeforeOpeningOrClosing + gardenMessageEnd;
				document.getElementById("gardenStatus").innerHTML = status;
			}

			else if (hours >= 17) {
				status = gardenClosedMessage;
				document.getElementById("gardenStatus").innerHTML = status;
			}

			didSetHours = true;
		}
	})

	return didSetHours;
}


function gardenYearlyHours() {
	// Code to account for Daylight Savings Time
	if ((month === 11 && day >= daylightEndDay) || (month === 12) || (month === 1) || (month === 2) || (month === 3 && day < daylightStartDay)) {
		hours = hours - 1;
	}

	// Between 8AM and 9AM: shows how many minutes before the garden opens
	if (hours === 8) {
		status = gardenWillOpenMessageStart + minutesBeforeOpeningOrClosing + gardenMessageEnd;
		document.getElementById("gardenStatus").innerHTML = status;

		return;
	}

	// TODO - Pass Concert objects to view so hours.js knows about early closing times
	/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
	/* CHANGE YEARLY: Early Closing Days for Concerts and Gala  								  */
	/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

	// Hours for individual concert days (which will change every year),
	// the Gala, and other miscellaneous days that we will close at 5PM

//#region Gala Month
	if (month === galaMonth && day === galaDay)		// Gala (if applicable)

	{
		busHours = "9AM-5PM";
		document.getElementById("gardenHours").innerHTML = busHours;
		otherNotes = "The Garden Will Close at 5PM for a Concert";

		if (month === galaMonth && day === galaDay) {
			otherNotes = "The Garden Will Close at 5PM for a Special Gala Event";
		}

		document.getElementById("otherNotes").innerHTML = otherNotes;

		if (hours >= 9 && hours < 16) {
			status = gardenOpenMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			return;
		}

		if (hours === 16) {
			status = gardenWillCloseMessageStart+minutesBeforeOpeningOrClosing+gardenMessageEnd;
			document.getElementById("gardenStatus").innerHTML = status;
			return;
		}

		else {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			return;
		}
	}
//#endregion

//#region Jan 1 - Mar 31 General Hours

	if (month === 1 || month === 2 || month === 3) {

		busHours = "Jan 2-Mar 31: 9AM-5PM";
		document.getElementById("gardenHours").innerHTML = busHours;

		if (month === 1 || month === 2) {
			admissionNotes = halfOffAdmission;
			document.getElementById("admissionDiscount").innerHTML =  admissionNotes;
		}


		if (month === 1 && day === 1) {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			otherNotes = "The Garden is Closed Dec 24-Jan 1";
			document.getElementById("otherNotes").innerHTML = otherNotes; // Note that we are closed Jan 1st
			return;
		}

		if (hours >= 9 && hours < 16) {
			status = gardenOpenMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			return;
		}

		if (hours === 16) {
			status = gardenWillCloseMessageStart+minutesBeforeOpeningOrClosing+gardenMessageEnd;
			document.getElementById("gardenStatus").innerHTML = status;
		}

		else {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
		}
	}
//#endregion

//#region April 1-30 General Hours

	else if (month === 4) {

		busHours = "Apr 1-30: 9AM-7:30PM";
		document.getElementById("gardenHours").innerHTML = busHours;

		if ((hours >= 9 && hours < 18) || (hours === 18 && minutes < 30)) {
			status = gardenOpenMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			return;
		}

		if ((hours === 18 && minutes >= 30) || (hours === 19 && minutes < 30)) {

			if (hours === 18 && minutes >= 30) {
				minutesBeforeOpeningOrClosing = (60 - minutes) + 30;
			}

			if (hours === 19 && minutes < 30) {
				minutesBeforeOpeningOrClosing = 30 - minutes;
			}

			status = gardenWillCloseMessageStart+minutesBeforeOpeningOrClosing+gardenMessageEnd;
			document.getElementById("gardenStatus").innerHTML = status;
		}

		else {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
		}
	}
//#endregion

//#region May 1 - Aug 31 General Hours

	else if (month === 5 || month === 6 || month === 7 || month === 8) {
		busHours = "May 1-Aug 31: 9AM-9PM*";
		otherNotes = "*Garden Hours on Concert Days: 9AM-5PM";
		document.getElementById("gardenHours").innerHTML = busHours;
		document.getElementById("otherNotes").innerHTML = otherNotes;

		// Checks if it's a concert day, else continues as normal
		if (isConcertDay(concerts, "Today (Concert Day): 9am-5pm"))
			return;

		if (hours >= 9 && hours < 20) {
			status = gardenOpenMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			return;
		}

		else if (hours === 20) {
			status = gardenWillCloseMessageStart+minutesBeforeOpeningOrClosing+gardenMessageEnd;
			document.getElementById("gardenStatus").innerHTML = status;
		}

		else {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
		}
	}
//#endregion

//#region  Sep 1 - 30 General Hours

	else if (month === 9) {
		busHours = "Sep 1-30: 9AM-7:30PM*";

		// Specific check for Teton Gravity Event on Sept. 20th; Will be removed on Sept. 21st
		if (day === 20)
			otherNotes = "*Garden Hours on Event Days: 9AM-5PM";
		else
			otherNotes = "*Garden Hours on Concert Days: 9AM-5PM";

		document.getElementById("gardenHours").innerHTML = busHours;
		document.getElementById("otherNotes").innerHTML = otherNotes;

		// Specific check for Teton Gravity Event on Sept. 20th; Will be removed on Sept. 21st
		if (day === 20 && isConcertDay(concerts, "Today (Garden Event): 9am-5pm"))
			return;

		// Checks if it's a concert day, else continues as normal
		if (isConcertDay(concerts, "Today (Concert Day): 9am-5pm"))
			return;

		if ((hours >= 9 && hours < 18) || (hours === 18 && minutes < 30)) {
			status = gardenOpenMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			return;
		}

		if ((hours === 18 && minutes >= 30) || (hours === 19 && minutes < 30)) {

			if (hours === 18 && minutes >= 30) {
				minutesBeforeOpeningOrClosing = (60 - minutes) + 30;
			}

			if (hours === 19 && minutes < 30) {
				minutesBeforeOpeningOrClosing = 30 - minutes;
			}

			status = gardenWillCloseMessageStart+minutesBeforeOpeningOrClosing+gardenMessageEnd;
			document.getElementById("gardenStatus").innerHTML = status;
		}

		else {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
		}
	}
//#endregion

//#region Oct 1 - Dec 23 General hours
	else if ( month === 10 || month === 11 || month === 12) {

		busHours = "Oct 1-Dec 23: 9AM-5PM";
		otherNotes = "Closed Thanksgiving Day and Dec 24-Jan 1";
		document.getElementById("gardenHours").innerHTML = busHours;
		document.getElementById("otherNotes").innerHTML = otherNotes;

		if (month === 12) {
			admissionNotes = halfOffAdmission;
			document.getElementById("admissionDiscount").innerHTML =  admissionNotes;
		}


		if ( (month === 10) && (day === gadDay1 || day === gadDay2 || day === gadDay3 || day === gadDay4 || day === gadDay5 || day === gadDay6) ) {
			otherNotes = "<div style=\x22color:#FF9100;font-weight:bold;\x22>The Garden will close at 5PM, then open again from 6-9PM for Garden After Dark</div>";
			document.getElementById("otherNotes").innerHTML = otherNotes;
			busHours = "9AM-5PM for General Admission<br />6PM-9PM for Garden After Dark";
			document.getElementById("gardenHours").innerHTML = busHours;

			if (hours >= 9 && hours < 16) {
				status = gardenOpenMessage;
				document.getElementById("gardenStatus").innerHTML = status;
				return;
			}

			if (hours === 16) {
				status = "<div style=\x22color:#FF9100;font-weight:bold;\x22>The Garden is Closing Soon, but will reopen at 6PM for Garden After Dark</div>";
				document.getElementById("gardenStatus").innerHTML = status;
				return;
			}

			if (hours >= 18 && hours < 20) {
				status = "<div style=\x22color:#FF9100;font-weight:bold;\x22>The Garden is Open for Garden After Dark!</div>";
				document.getElementById("gardenStatus").innerHTML = status;
				return;
			}

			if (hours === 20) {
				status = gardenWillCloseMessageStart+minutesBeforeOpeningOrClosing+gardenMessageEnd;
				document.getElementById("gardenStatus").innerHTML = status;
				return;
			}

			else {
				status = gardenClosedMessage;
				document.getElementById("gardenStatus").innerHTML = status;
				return;
			}
		}


		if (month === 11 && day === thanksgivingDay) {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			busHours = "";
			document.getElementById("gardenHours").innerHTML = busHours;
			otherNotes = "The Garden is Closed for the Thanksgiving Holiday";
			document.getElementById("otherNotes").innerHTML = otherNotes;
			return;
		}



		// Shows message that we will close for holiday party on the day before holiday party
		if (month === 12 && day === (holidayPartyDay - 1)) {
			otherNotes = "The Garden Will Close Early Tomorrow at 2PM";
			document.getElementById("otherNotes").innerHTML =  otherNotes;
			return;
		}

		// Changes business hours to those of holiday party and adds note for public
		if (month === 12 && day === holidayPartyDay) {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			busHours = "9AM-2PM";
			document.getElementById("gardenHours").innerHTML = busHours;
			otherNotes = "The Garden Will Close Early for our Annual Staff Holiday Party";
			document.getElementById("otherNotes").innerHTML = otherNotes;

			if ( (hours >= 9) && (hours < holidayPartyClosingHour) ) {
				status = gardenOpenMessage;
				document.getElementById("gardenStatus").innerHTML = status;
				return;
			}

			else if ( ( (hours === holidayPartyClosingHour - 1) && (minutes < holidayPartyClosingMinute) ) ) {
				status = gardenWillCloseMessageStart+minutesBeforeOpeningOrClosing+gardenMessageEnd;
				document.getElementById("gardenStatus").innerHTML = status;
				return;
			}

			else {
				status = gardenClosedMessage;
				document.getElementById("gardenStatus").innerHTML = status;
				return;
			}

		}

		if (month === 12 && day >= 24) {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
			busHours = "";
			document.getElementById("gardenHours").innerHTML = busHours;
			otherNotes = "The Garden is Closed Dec 24-Jan 1";
			document.getElementById("otherNotes").innerHTML = otherNotes;
		}

		else if (hours >= 9 && hours < 16) {
			status = gardenOpenMessage;
			document.getElementById("gardenStatus").innerHTML = status;
		}

		else if (hours === 16) {
			status = gardenWillCloseMessageStart+minutesBeforeOpeningOrClosing+gardenMessageEnd;
			document.getElementById("gardenStatus").innerHTML = status;
		}

		else {
			status = gardenClosedMessage;
			document.getElementById("gardenStatus").innerHTML = status;
		}
	}
//#endregion
}
