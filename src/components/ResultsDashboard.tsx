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

interface ResultsDashboardProps {
  results: {
    qualificationScore: number;
    monthlyIncome: number[];
    monthlyExpenses: number[];
    balanceTrend: number[];
    months: string[];
  };
  onReset: () => void;
}

export const ResultsDashboard = ({ results, onReset }: ResultsDashboardProps) => {
  const chartData = results.months.map((month, index) => ({
    month,
    income: results.monthlyIncome[index],
    expenses: results.monthlyExpenses[index],
    balance: results.balanceTrend[index],
  }));

  return (
    <div className="space-y-8">
      <Button
        variant="ghost"
        className="flex items-center gap-2"
        onClick={onReset}
      >
        <ArrowLeft className="w-4 h-4" /> Upload Another Statement
      </Button>

      <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
        <Card className="p-6">
          <h3 className="text-lg font-medium mb-2">Qualification Score</h3>
          <div className="flex items-center justify-center h-32">
            <div className="text-5xl font-bold text-primary">
              {results.qualificationScore}%
            </div>
          </div>
        </Card>

        <Card className="p-6 md:col-span-2">
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

        <Card className="p-6 md:col-span-2 lg:col-span-3">
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
      </div>
    </div>
  );
};