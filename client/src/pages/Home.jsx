import { useEffect, useState } from "react";
import "../styles/style.css";
import ArrowBackIosNewIcon from "@mui/icons-material/ArrowBackIosNew";
import ArrowForwardIosIcon from "@mui/icons-material/ArrowForwardIos";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";

import Toolbar from "@mui/material/Toolbar";
import Button from "@mui/material/Button";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
import Typography from "@mui/material/Typography";
import Link from "@mui/material/Link";

function Home() {
	const [topics, setTopics] = useState([]);
	const [summaries, setSummaries] = useState([]);

	const [age, setAge] = useState("");

	const handleChange = (event) => {
		setAge(event.target.value);
	};

	useEffect(() => {
		fetchTopics();
		//fetchSummaries();
	}, []);

	const fetchTopics = async () => {
		const response = await fetch("http://127.0.0.1:5000/api/topics");
		const data = await response.json();
		setTopics(data.topics);
		console.log(data.topics);
	};

	const fetchSummaries = async () => {
		const response = await fetch("http://127.0.0.1:5000/api/summaries");
		const data = await response.json();
		setTopics(data.summaries);
	};

	const fetchStories = async () => {
		const response = await fetch("http://127.0.0.1:5000/api/stories");
		const data = await response.json();
		setTopics(data.stories);
	};

	// Space to content. Show top most summaries
	// Sort by date
	// On click at top filter by league
	return (
		<>
			<div className="flexbox-container">
				<div>
					<ArrowBackIosNewIcon className="arrows" />
				</div>
				<div>
					<h3> Today </h3>
				</div>
				<div>
					<a className="btn">
						<ArrowForwardIosIcon className="arrows disabled" />
					</a>
				</div>
			</div>

			<div className="container feed">
				<div className="row">
					<h1>Headline</h1>
					<p>Story being summarized for the feed</p>
				</div>
			</div>
		</>
	);
}

export default Home;

/*
<div className="flexbox-container">
				<div className="row">
					<FormControl sx={{ m: 1, minWidth: 120 }}>
						<Select
							value={age}
							onChange={handleChange}
							displayEmpty
						>
							<MenuItem value="">
								<em>ALL</em>
							</MenuItem>
							<MenuItem value={10}>MLB</MenuItem>
							<MenuItem value={20}>NBA</MenuItem>
							<MenuItem value={30}>NFL</MenuItem>
						</Select>
					</FormControl>
				</div>
			</div>
*/
