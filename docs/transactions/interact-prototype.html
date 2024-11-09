<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UETA Tips and Scenarios</title>
    <script src="https://unpkg.com/react@17/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
        const SideBySideComparison = () => {
            const [selectedTip, setSelectedTip] = React.useState(null);
            const [selectedScenario, setSelectedScenario] = React.useState(null);
            const [orderedTips, setOrderedTips] = React.useState([]);
            const [orderedScenarios, setOrderedScenarios] = React.useState([]);

            const tipsData = [
                { 
                    id: 1, 
                    title: "Implement Clear Attribution Mechanisms", 
                    content: "Ensure AI agents have clear and reliable ways to indicate on whose behalf they are operating.",
                    relatedScenarios: [1, 2]
                },
                { 
                    id: 2, 
                    title: "Explicit Consideration of Consent and Intent", 
                    content: "Develop systems designed to capture explicit consent from users before executing transactions.",
                    relatedScenarios: [1, 3]
                },
                { 
                    id: 3, 
                    title: "Develop Robust Error Detection and Correction Protocols", 
                    content: "Implement systems that can detect changes or errors in transactions and provide opportunities for correction.",
                    relatedScenarios: [2, 3]
                }
            ];

            const scenariosData = [
                { 
                    id: 1, 
                    title: "Online Shopping Agent", 
                    content: "An AI agent makes purchases on behalf of a user without explicit approval for each transaction.",
                    relatedTips: [1, 2]
                },
                { 
                    id: 2, 
                    title: "Automated Bill Payment", 
                    content: "An AI agent manages recurring payments and encounters an unexpectedly high bill.",
                    relatedTips: [1, 3]
                },
                { 
                    id: 3, 
                    title: "Travel Booking Agent", 
                    content: "An AI agent books a non-refundable flight and hotel package without clear user consent.",
                    relatedTips: [2, 3]
                }
            ];

            React.useEffect(() => {
                setOrderedTips(tipsData);
                setOrderedScenarios(scenariosData);
            }, []);

            const handleTipClick = (tipId) => {
                setSelectedTip(tipId);
                setSelectedScenario(null);
                reorderTips(tipId);
            };

            const handleScenarioClick = (scenarioId) => {
                setSelectedScenario(scenarioId);
                setSelectedTip(null);
                reorderScenarios(scenarioId);
            };

            const reorderTips = (tipId) => {
                const selectedTipIndex = orderedTips.findIndex(t => t.id === tipId);
                if (selectedTipIndex > 0) {
                    const newOrder = [
                        orderedTips[selectedTipIndex],
                        ...orderedTips.slice(0, selectedTipIndex),
                        ...orderedTips.slice(selectedTipIndex + 1)
                    ];
                    setOrderedTips(newOrder);
                }
            };

            const reorderScenarios = (scenarioId) => {
                const selectedScenarioIndex = orderedScenarios.findIndex(s => s.id === scenarioId);
                if (selectedScenarioIndex > 0) {
                    const newOrder = [
                        orderedScenarios[selectedScenarioIndex],
                        ...orderedScenarios.slice(0, selectedScenarioIndex),
                        ...orderedScenarios.slice(selectedScenarioIndex + 1)
                    ];
                    setOrderedScenarios(newOrder);
                }
            };

            const linkStyle = {
                color: 'blue',
                textDecoration: 'underline',
                cursor: 'pointer'
            };

            return (
                <div style={{ display: 'flex', flexDirection: 'row', gap: '20px' }}>
                    <div style={{ flex: 1 }}>
                        <h2 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '16px' }}>Tips</h2>
                        {orderedTips.map(tip => (
                            <div 
                                key={tip.id} 
                                style={{
                                    border: selectedTip === tip.id ? '2px solid blue' : '1px solid #ccc',
                                    borderRadius: '4px',
                                    padding: '16px',
                                    marginBottom: '16px',
                                    cursor: 'pointer'
                                }}
                                onClick={() => handleTipClick(tip.id)}
                            >
                                <h3 style={{ fontSize: '18px', fontWeight: 'bold', marginBottom: '8px' }}>{tip.title}</h3>
                                <p>{tip.content}</p>
                                {selectedTip === tip.id && (
                                    <div style={{ marginTop: '16px' }}>
                                        <h4 style={{ fontWeight: 'bold' }}>Related Scenarios:</h4>
                                        <ul>
                                            {tip.relatedScenarios.map(scenarioId => (
                                                <li key={scenarioId}>
                                                    <span 
                                                        style={linkStyle}
                                                        onClick={(e) => {
                                                            e.stopPropagation();
                                                            handleScenarioClick(scenarioId);
                                                        }}
                                                    >
                                                        {scenariosData.find(s => s.id === scenarioId).title}
                                                    </span>
                                                </li>
                                            ))}
                                        </ul>
                                    </div>
                                )}
                            </div>
                        ))}
                    </div>
                    <div style={{ flex: 1 }}>
                        <h2 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '16px' }}>Scenarios</h2>
                        {orderedScenarios.map(scenario => (
                            <div 
                                key={scenario.id} 
                                style={{
                                    border: selectedScenario === scenario.id ? '2px solid green' : '1px solid #ccc',
                                    borderRadius: '4px',
                                    padding: '16px',
                                    marginBottom: '16px',
                                    cursor: 'pointer'
                                }}
                                onClick={() => handleScenarioClick(scenario.id)}
                            >
                                <h3 style={{ fontSize: '18px', fontWeight: 'bold', marginBottom: '8px' }}>{scenario.title}</h3>
                                <p>{scenario.content}</p>
                                {selectedScenario === scenario.id && (
                                    <div style={{ marginTop: '16px' }}>
                                        <h4 style={{ fontWeight: 'bold' }}>Related Tips:</h4>
                                        <ul>
                                            {scenario.relatedTips.map(tipId => (
                                                <li key={tipId}>
                                                    <span 
                                                        style={linkStyle}
                                                        onClick={(e) => {
                                                            e.stopPropagation();
                                                            handleTipClick(tipId);
                                                        }}
                                                    >
                                                        {tipsData.find(t => t.id === tipId).title}
                                                    </span>
                                                </li>
                                            ))}
                                        </ul>
                                    </div>
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            );
        };

        ReactDOM.render(
            <React.StrictMode>
                <h1 style={{ fontSize: '32px', fontWeight: 'bold', marginBottom: '24px' }}>UETA Tips and Scenarios</h1>
                <SideBySideComparison />
            </React.StrictMode>,
            document.getElementById('root')
        );
    </script>
</body>
</html>
