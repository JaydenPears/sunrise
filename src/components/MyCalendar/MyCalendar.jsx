// import libs:
import { useMemo } from 'react';
import { Calendar, dateFnsLocalizer, Views } from 'react-big-calendar';
import format from 'date-fns/format';
import parse from 'date-fns/parse';
import startOfWeek from 'date-fns/startOfWeek';
import getDay from 'date-fns/getDay';
import ru from 'date-fns/locale/ru';
import moment from 'moment';

// include static:
import './MyCalendar.css';
import "react-big-calendar/lib/addons/dragAndDrop/styles.css";
import "react-big-calendar/lib/css/react-big-calendar.css";

const locales = {
	'ru': ru,
};

const localizer = dateFnsLocalizer({
	format,
	parse,
	startOfWeek,
	getDay,
	locales,
});

const myEventsList = [
	{
		start: moment().toDate(),
		end: moment().add(0, "days").toDate(),
		title: "16:30\n-\n19:30",
	},
]

const MyCalendar = () => {
	const { defaultDate, views } = useMemo(
		() => ({
		  defaultDate: moment().toDate(),
		  views: [Views.MONTH],
		}),
		[]
	)

	return (
		<Calendar
			localizer={localizer}
			events={myEventsList}
			startAccessor="start"
			endAccessor="end"
			views={views}
			defaultDate={defaultDate}
			style={{ height: 500 }}
    	/>
	)
};

export default MyCalendar;