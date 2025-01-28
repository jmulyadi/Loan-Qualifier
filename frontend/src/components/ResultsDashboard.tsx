import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { ArrowLeft } from "lucide-react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";
import { motion } from "framer-motion"; // Import motion

interface ResultsDashboardProps {
  results: {
    qualificationScore: number;
    monthlyIncome: number[];
    monthlyExpenses: number[];
    balanceTrend: number[];
    months: string[];
    summary: string;
  };
  onReset: () => void;
}

export const ResultsDashboard = ({
  results,
  onReset,
}: ResultsDashboardProps) => {
  const chartData = results.months.map((month, index) => ({
    month,
    income: results.monthlyIncome[index],
    expenses: results.monthlyExpenses[index],
    balance: results.balanceTrend[index],
  }));

  return (
    <div className="space-y-8">
      {/* Reset Button */}
      <Button
        variant="ghost"
        className="flex items-center gap-2"
        onClick={onReset}
      >
        <ArrowLeft className="w-4 h-4" /> Upload Another Statement
      </Button>
      <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
        {/* Summary Section */}
        <motion.div
          className="md:col-span-2 lg:col-span-3"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <Card className="p-6">
            <h3 className="text-lg font-medium mb-2">Why You Got This Score</h3>
            <p className="text-muted-foreground">{results.summary}</p>
          </Card>
        </motion.div>

        {/* Qualification Score with Percentage Circle */}
        <motion.div
          className=""
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5 }}
        >
          <Card className="p-6">
            <h3 className="text-lg font-medium mb-4 text-center">
              Qualification Score
            </h3>
            <div className="flex items-center justify-center h-32">
              <div className="">
                {" "}
                {/* Set a fixed width and height for the container */}
                <CircularProgressbar
                  value={results.qualificationScore}
                  text={`${results.qualificationScore}%`}
                  styles={buildStyles({
                    textColor: "#ffffff",
                    textSize: "16px",
                    strokeLinecap: "butt",
                    pathTransitionDuration: 0.5,
                    pathColor: `rgb(${255 - results.qualificationScore * 2.55}, ${
                      results.qualificationScore * 2.55
                    }, 0)`,
                    trailColor: "#f0f0f0",
                  })}
                  circleRatio={0.99}
                />
              </div>
            </div>
          </Card>
        </motion.div>

        {/* Monthly Cash Flow Card */}
        <motion.div
          className="md:col-span-2"
          initial={{ opacity: 0, x: -50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5 }}
        >
          <Card className="p-6">
            <h3 className="text-lg font-medium mb-4">Monthly Cash Flow</h3>
            <div className="h-[300px]">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Line
                    type="monotone"
                    dataKey="income"
                    stroke="#0EA5E9"
                    name="Income"
                  />
                  <Line
                    type="monotone"
                    dataKey="expenses"
                    stroke="#F43F5E"
                    name="Expenses"
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </Card>
        </motion.div>

        {/* Balance Trend Card */}
        <motion.div
          className="md:col-span-2 lg:col-span-3"
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5 }}
        >
          <Card className="p-6">
            <h3 className="text-lg font-medium mb-4">Balance Trend</h3>
            <div className="h-[300px]">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Line
                    type="monotone"
                    dataKey="balance"
                    stroke="#22C55E"
                    name="Balance"
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </Card>
        </motion.div>
      </div>
    </div>
  );
};

