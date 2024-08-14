import { useEffect, useState } from "react";
import "./App.css";

function App() {
	const [topics, setTopics] = useState([]);

	useEffect(() => {
		fetchTopics();
	}, []);

	const fetchTopics = async () => {
		const response = await fetch("http://127.0.0.1:5000/api/topics");
		const data = await response.json();
		setTopics(data.topics);
	};

	return <>Hello World</>;
}

export default App;
