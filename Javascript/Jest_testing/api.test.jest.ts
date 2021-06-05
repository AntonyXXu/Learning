import { describe, it, expect } from "@jest/globals";
import { TextEncoder } from "util";
import { MyLambdaClient } from "aws-sdk";

const LambdaClient = new MyLambdaClient();

describe("lambda fcn client-config-svc", () => {
  it("GET /api/clients can respond", async () => {
    //Arrange
    const data = new TextEncoder().encode(
      JSON.stringify({
        path: "/client-config-svc//api/clients",
        httpMethod: "GET",
      })
    );
    const expected = ["niagara-wineries"];
    const notExpected = ["testName1", "testName2"];

    //Act
    const response = await LambdaClient.invoke({
      FunctionName: "client-config-svc",
      payload: data,
    });

    //Assert
    expect(response.statusCode).toBe(200);
    expect(typeof response.body).toBe(Array);
    expect(response.body).toEqual(expect.arrayContaining(expected));
    expect(response.body).not.toEqual(expect.arrayContaining(notExpected));
  });

  it("GET /api/clients/{clientName} can respond", async () => {
    //Arrange
    const clientID = "niagara-wineries";
    const data = new TextEncoder().encode(
      JSON.stringify({
        path: `/client-config-svc/api/clients/${clientID}`,
        httpMethod: "GET",
      })
    );
    //Act
    const response = await LambdaClient.invoke({
      FunctionName: "client-config-svc",
      payload: data,
    });
    //Assert
    expect(response.statusCode).toBe(200);
    expect(response.body).toHaveProperty("clientID");
    expect(response.body).toHaveProperty("clientName");
    expect(response.body).toHaveProperty("brand");
    expect(response.body).toHaveProperty("industry");
    expect(response.body).toHaveProperty("status");
    expect(response.body).toHaveProperty("country");
  });
});
